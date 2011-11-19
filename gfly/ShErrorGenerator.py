#-*- coding:utf-8 -*-
import re
import subprocess

class ShErrorGenerator:
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
		ps_sh = subprocess.Popen(["sh", "-n", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_sh.stderr:
				print line[length:]
				matchObj = re.search("^:\s*[0-9]+:", line[length:])
				if not matchObj is None:
					errorLine 	= int(matchObj.group(0)[1:-1])
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = line.replace(filepath, filename).strip()
						yield errorLine
					continue
		finally:
			ps_sh.stderr.close()
