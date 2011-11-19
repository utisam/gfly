#-*- coding:utf-8 -*-
import os
import re
import subprocess

class JavaErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
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
				matchObj = re.search("^:([0-9]+):(.*)", line[length:])
				if not matchObj is None:
					errorLine = int(matchObj.group(1))
					if not self.errorLineMsg.has_key(errorLine):
						self.errorLineMsg[errorLine] = matchObj.group(2).strip()
						yield errorLine
		finally:
			ps_javac.stdout.close()
			ps_javac.stderr.close()
