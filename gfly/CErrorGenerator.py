#-*- coding:utf-8 -*-
import re
import subprocess

class CErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		#for gcc
		ps_gcc = subprocess.Popen(["gcc", "-Wall", "-lm", "-fsyntax-only", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_gcc.stderr:
				matchObj = re.search("^:[0-9]+:", line[length:])
				if not matchObj is None:
					errorLine = int(matchObj.group(0)[1:-1])
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = line[length + matchObj.end():].strip()
						yield errorLine
		finally:
			ps_gcc.stderr.close()
