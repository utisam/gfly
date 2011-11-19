#-*- coding:utf-8 -*-
import re
import subprocess

class CErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, doc):
		"""generate error lines
		if there are Makefile in doc's dir, use that.
		if no Makefile, use "gcc -Wall -lm"
		and parse output.
		"""
		#print "uri: " + doc.get_uri()
		filepath = doc.get_uri_for_display()
		#print "get_uri_for_display: " + filepath
		#print "short_name_for_display: " + doc.get_short_name_for_display()
		#dirname = os.path.dirname(filepath)
		#for gcc
		#sExt = re.search("\.[^\.]*$", filepath).start()
		ps_gcc = subprocess.Popen(["gcc", "-Wall", "-lm", "-fsyntax-only", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_gcc.stderr:
				matchObj = re.search("^:[0-9]+:", line[length:])
				if matchObj is None:
					continue
				errorLine = int(matchObj.group(0)[1:-1])
				if not self.errorLineMsg.has_key(errorLine):
					self.errorLineMsg[errorLine] = line[length + matchObj.end():].strip()
					yield errorLine
		finally:
			ps_gcc.stderr.close()
