#-*- coding:utf-8 -*-
import os
import re
import subprocess

class JavaErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, doc):
		"""generate error lines
		"""
		#print "uri: " + doc.get_uri()
		filepath = doc.get_uri_for_display()
		#print "get_uri_for_display: " + filepath
		#print "short_name_for_display: " + doc.get_short_name_for_display()
		#dirname = os.path.dirname(filepath)
		#for javac
		if os.path.exists("/tmp") and os.access("/tmp", os.W_OK):
			if not os.path.exists("/tmp/gfly"):
				os.mkdir("/tmp/gfly")
			ps_javac = subprocess.Popen(["javac", filepath, "-d", "/tmp/gfly"],
						stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			ps_javac = subprocess.Popen(["javac", filepath],
						stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_javac.stderr:
				matchObj = re.search("^:[0-9]+:", line[length:])
				if matchObj is None:
					continue
				errorLine = int(matchObj.group(0)[1:-1])
				if not self.errorLineMsg.has_key(errorLine):
					self.errorLineMsg[errorLine] = line[length + matchObj.end():].strip()
					yield errorLine
		finally:
			ps_javac.stdout.close()
			ps_javac.stderr.close()
