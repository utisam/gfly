#-*- coding:utf-8 -*-
import threading
import gtk
import pango
import gedit

from CErrorGenerator import CErrorGenerator
from CppErrorGenerator import CppErrorGenerator
from JavaErrorGenerator import JavaErrorGenerator
from JavascriptErrorGenerator import ClosureLinterErrorGenerator
#from PythonErrorGenerator import PylintErrorGenerator
from PythonErrorGenerator import PyflakesErrorGenerator
from CsharpErrorGenerator import CsharpErrorGenerator
from PerlErrorGenerator import PerlErrorGenerator
from PhpErrorGenerator import PhpErrorGenerator
from RubyErrorGenerator import RubyErrorGenerator
from ShErrorGenerator import ShErrorGenerator
from LatexErrorGenerator import LatexErrorGenerator
""" when you want to add error generator, use under map, and add instance.
ErrorGenerator needs "errorLineMsg(Map)" and "def generateErrorLines(self, doc):"
key: language name using gedit
value: list of generator
"""
errorGenerator = {
	"C": [CErrorGenerator()],
	"C++": [CppErrorGenerator()],
	"C/C++/ObjC Header": [CppErrorGenerator()],
	"C#": [CsharpErrorGenerator()],
	"Java": [JavaErrorGenerator()],
	"Javascript": [ClosureLinterErrorGenerator()],
	"Python": [PyflakesErrorGenerator()],#[PylintErrorGenerator()],
	"Perl": [PerlErrorGenerator()],
	"PHP": [PhpErrorGenerator()],
	"Ruby": [RubyErrorGenerator()],
	"sh": [ShErrorGenerator()],
	"LaTeX": [LatexErrorGenerator()],
}

# key binding
jump_to_error_key = "<Control>1"

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
	""" get two gtk.TextIter, start and end of line
	Attribute:
		line: integer of line number(start 0)
	"""
	s = doc.get_iter_at_line(line)
	e = s.copy()
	e.forward_line()
	return s, e
def skipWhiteSpaces(itr):
	while not itr.starts_word() and itr.forward_char():
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
	currentDocConnected = None
	errorTag = None
	def __init__(self, window):
		self.geditWindow = window
		#connect sindow signal
		self.tabConnected = []
#		self.tabConnected.append(self.geditWindow.connect("tab_added", self.__tab_added))
		self.tabConnected.append(window.connect("active_tab_changed", self.__tab_changed))
#		self.tabConnected.append(self.geditWindow.connect("tab_removed", self.__tab_removed))
	def __del__(self):
		#disconnect signal
		for i in self.tabConnected:
			self.geditWindow.disconnect(i)
		if not self.currentDocConnected is None:
			self.geditWindow.disconnect(currentDocConnected)
#	def __tab_added(self, window, tab):
#		pass
	def __tab_changed(self, window, tab):
		#connect document signal
		if not self.currentDocConnected is None:
			window.disconnect(currentDocConnected)
		doc = window.get_active_document()
		doc.connect("saved", self.__doc_saved)
		#connect view signal
		tab.get_view().connect_after("move-cursor", self.__move_cursor)
		#create tag for error
		self.errorTag = doc.get_tag_table().lookup('errorTag')
		if self.errorTag == None:
			self.errorTag = doc.create_tag('errorTag', underline=pango.UNDERLINE_ERROR)
		self.draw_lines(doc)
#	def __tab_removed(self, window, tab):
#		pass
	def __doc_saved(self, doc, *args):
		self.draw_lines(doc)
	def draw_lines(self, doc):
		lang = getLanguageName(doc)
		if errorGenerator.has_key(lang):
			#generate error and apply new error tag
			s, e = doc.get_bounds()
			doc.remove_tag(self.errorTag, s, e)
			for g in errorGenerator[lang]:
				try:
					for i in g.generateErrorLines(doc.get_uri_for_display()):
						s, e = getLineStartToEnd(doc, i - 1)
						doc.apply_tag(self.errorTag, skipWhiteSpaces(s), e)
				except Error:
					print "cannot generateErrorLines"
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

class gfly(gedit.Plugin):
	def __init__(self):
		gedit.Plugin.__init__(self)
	def activate(self, window):
		global ui_str
		self.tabwatch = TabWatch(window)
		manager = window.get_ui_manager()
		self.action_group = gtk.ActionGroup("gflyPluginAction")
		self.action_group.add_actions([("gfly", None, "Jump Error", jump_to_error_key, None, self.__jump_error)])
		manager.insert_action_group(self.action_group, -1)
		self.ui_id = manager.add_ui_from_string(ui_str)
	def deactivate(self, window):
		pass
	def update_ui(self, window):
		pass
	def __jump_error(self, action):
		self.tabwatch.jump_error()
