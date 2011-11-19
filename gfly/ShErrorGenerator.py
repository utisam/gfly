#-*- coding:utf-8 -*-
import re
import subprocess

class ShErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		#for sh -n
		ps_sh = subprocess.Popen(["sh", "-n", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		length = len(filepath)
		try:
			for line in ps_sh.stderr:
				matchObj = re.search("^:\s*([0-9]+): (.*)", line[length:])
				if not matchObj is None:
					errorLine 	= int(matchObj.group(1))
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = matchObj.group(2).strip()
						yield errorLine
		finally:
			ps_sh.stderr.close()
