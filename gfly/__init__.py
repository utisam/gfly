	#-*- coding:utf-8 -*-
import string
from gi.repository import GObject, Gedit, Gtk, Pango
from settings import errorGenerator, jump_to_error_key, notification

ui_str = """<ui>
	<menubar name="MenuBar">
		<menu name="EditMenu" action="Edit">
			<placeholder name="EditOps_6">
				<menuitem name="gfly" action="gfly"/>
			</placeholder>
		</menu>
	</menubar>
</ui>
"""

def getLineStartToEnd(doc, line):
	""" get two Gtk.TextIter, start and end of line
	Attribute:
		line: integer of line number(start 0)
	"""
	s = doc.get_iter_at_line(line)
	e = s.copy()
	e.forward_line()
	return s, e
def skipWhiteSpaces(itr):
	""" skip white spaces of Gtk.TextIter
	"""
	while itr.get_char() in string.whitespace and itr.forward_char():
		pass
	return itr
def getLanguageName(doc):
	""" get document's languageName
	Attribute:
		doc: GeditDocument
	"""
	lang = doc.get_language()
	if lang:
		return lang.get_name()

class TabWatch:
	def __init__(self, window):
		self.errorTag = None
		self.currentConnectedTab = None
		self.currentConnectedDoc = None
		self.geditWindow = window
		#connect sindow signal
		self.currentConnectedTab = window.connect("active_tab_changed", self.__tab_changed)
	def close(self, window):
		if not self.currentConnectedTab is None:
			window.disconnect(self.currentConnectedTab)
			self.currentConnectedTab = None
		if not self.currentConnectedDoc is None:
			window.disconnect(self.currentConnectedDoc)
			self.currentConnectedDoc = None
	def __tab_changed(self, window, tab):
		doc = window.get_active_document()
		#connect sindow signal
		if not self.currentConnectedTab is None:
			window.disconnect(self.currentConnectedTab)
			self.currentConnectedTab = None
		self.currentConnectedTab = window.connect("active_tab_changed", self.__tab_changed)
		#connect document signal
		if not self.currentConnectedDoc is None:
			window.disconnect(self.currentConnectedDoc)
			self.currentConnectedDoc = None
		doc.connect("saved", self.__doc_saved)
		#connect view signal
		tab.get_view().connect_after("move-cursor", self.__move_cursor)
		#create tag for error
		self.errorTag = doc.get_tag_table().lookup('errorTag')
		if self.errorTag is None:
			self.errorTag = doc.create_tag('errorTag', underline=Pango.Underline.ERROR)
		self.draw_lines(doc)
	def __doc_saved(self, doc, *args):
		self.draw_lines(doc)
	def draw_lines(self, doc):
		# clear
		s, e = doc.get_bounds()
		doc.remove_tag(self.errorTag, s, e)
		#generate error and apply new error tag
		lang = getLanguageName(doc)
		if errorGenerator.has_key(lang):
			errorCount = 0
			for g in errorGenerator[lang]:
				try:
					for i in g.generateErrorLines(doc.get_uri_for_display()):
						s, e = getLineStartToEnd(doc, i - 1)
						doc.apply_tag(self.errorTag, skipWhiteSpaces(s), e)
						errorCount += 1
				except EnvironmentError:
					print "cannot generateErrorLines"
			if notification:
				self.errorNorify(errorCount)
	def errorNorify(self, count):
		if count <= 0:
			return
		try:
			import pynotify
			pynotify.init("gfly_notify")
			if count == 1:
				n = pynotify.Notification("gfly", "There is one error")
			else:
				n = pynotify.Notification("gfly", "There are %d error" % count)
			n.show()
		except ImportError:
			pass
	def __move_cursor(self, textview, *args):
		global errorGenerator
		doc = textview.get_buffer()
		lang = getLanguageName(doc)
		if errorGenerator.has_key(lang):
			textview.set_has_tooltip(False)
			cursorIter = doc.get_iter_at_mark(doc.get_insert())
			cursorLine = cursorIter.get_line()
			for g in errorGenerator[lang]:
				if g.errorLineMsg.has_key(cursorLine + 1):
					textview.set_has_tooltip(True)
					textview.set_tooltip_text(g.errorLineMsg[cursorLine + 1])
	def jump_error(self):
		view = self.geditWindow.get_active_view()
		doc = view.get_buffer()
		lang = getLanguageName(doc)
		if errorGenerator.has_key(lang):
			cursorLine = doc.get_iter_at_mark(doc.get_insert()).get_line()
			lines = []
			for g in errorGenerator[lang]:
				lines.extend(g.errorLineMsg.keys())
			if len(lines) != 0:
				lines.sort()
				for i in lines:
					if cursorLine < i - 1:
						doc.goto_line(i - 1)
						view.scroll_to_cursor()
						return
				doc.goto_line(lines[0] - 1)
				view.scroll_to_cursor()

class gfly(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "gfly"
	window = GObject.property(type=Gedit.Window)
	def __init__(self):
		GObject.Object.__init__(self)
	def do_activate(self):
		global ui_str
		self.tabwatch = TabWatch(self.window)
		manager = self.window.get_ui_manager()
		self.action_group = Gtk.ActionGroup("gflyPluginAction")
		self.action_group.add_actions([("gfly", None, "Jump Error", jump_to_error_key, None, self.__jump_error)])
		manager.insert_action_group(self.action_group, -1)
		self.ui_id = manager.add_ui_from_string(ui_str)
	def do_deactivate(self):
		self.tabwatch.close(self.window)
	def do_update_state(self):
		pass
	def __jump_error(self, action):
		self.tabwatch.jump_error()
