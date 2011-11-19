#-*- coding:utf-8 -*-
import re
import subprocess

class PythonErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, doc):
		"""generate error lines
		"""
		#print "uri: " + doc.get_uri()
		filepath = doc.get_uri_for_display()
		#print "get_uri_for_display: " + filepath
		#filename = doc.get_short_name_for_display()
		#print "short_name_for_display: " + filename
		#for pylint
		ps_pylint = subprocess.Popen(["pylint", "-E", filepath],
					stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		try:
			for line in ps_pylint.stdout:
				matchObj = re.search("^E: *[0-9]*: ", line)
				if not matchObj is None:
					errorLine = int(matchObj.group(0)[2:-2])
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = line[matchObj.end():].strip()
						yield errorLine
					continue
		finally:
			ps_pylint.stdout.close()
			ps_pylint.stderr.close()
