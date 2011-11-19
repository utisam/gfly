#-*- coding:utf-8 -*-
import re
import subprocess

class PerlErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		ps_pych = subprocess.Popen(["perl", "-wc", filepath],
					#stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
		self.errorLineMsg.clear()
		try:
			for line in ps_pych.stderr:
				matchObj = re.search("(.*) line ([0-9]+)\.$", line)
				if not matchObj is None:
					errorLine = int(matchObj.group(2))
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = matchObj.group(1).strip()
						yield errorLine
		finally:
			ps_pych.stderr.close()
