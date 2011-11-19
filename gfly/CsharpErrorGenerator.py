#-*- coding:utf-8 -*-
import re
import subprocess

class CsharpErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		#for mono(gmcs)
		ps_mono = subprocess.Popen(["gmcs", filepath],
					stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_mono.stderr:
				matchObj = re.search("^\(([0-9]+),[0-9]+\): (.*)", line[length:])
				if not matchObj is None:
					errorLine = int(matchObj.group(1))
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = matchObj.group(2).strip()
						yield errorLine
		finally:
			ps_mono.stderr.close()
