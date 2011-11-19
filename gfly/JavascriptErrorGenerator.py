#-*- coding:utf-8 -*-
import re
import subprocess

class ClosureLinterErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		#for sh -n
		ps_sh = subprocess.Popen(["gjslint", filepath],
					stdout=subprocess.PIPE,)
		self.errorLineMsg.clear()
		try:
			for line in ps_sh.stdout:
				matchObj = re.search("^Line ([0-9]+), .:\d\d\d\d: (.*)", line)
				if not matchObj is None:
					errorLine 	= int(matchObj.group(1))
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = matchObj.group(2).strip()
						yield errorLine
		finally:
			ps_sh.stdout.close()
