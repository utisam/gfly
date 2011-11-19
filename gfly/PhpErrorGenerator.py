#-*- coding:utf-8 -*-
import re
import subprocess

class PhpErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, doc):
		"""generate error lines
		"""
		#print "uri: " + doc.get_uri()
		filepath = doc.get_uri_for_display()
		#print "get_uri_for_display: " + filepath
		filename = doc.get_short_name_for_display()
		#print "short_name_for_display: " + filename
		#for pychecker
		ps_pych = subprocess.Popen(["php", "-l", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		try:
			for line in ps_pych.stderr:
				matchObj = re.search("line [0-9]+$", line)
				if not matchObj is None:
					errorLine = int(matchObj.group(0)[5:])
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = line.replace(filepath, filename).strip()
						yield errorLine
					continue
		finally:
			ps_pych.stderr.close()
