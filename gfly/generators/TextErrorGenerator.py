#-*- coding:utf-8 -*-
import re

class TextErrorGenerator:
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		self.errorLineMsg.clear()
		with open(filepath) as f:
			assertRegex = None
			settingRegex = re.compile(r"[\*#%;(?://)] textassert(.*):(.*)")
			for i, line in enumerate(f):
				lineNum = i + 1
				if not assertRegex is None:
					if re.search(assertRegex, line):
						self.errorLineMsg[lineNum] = "hit!"
						yield lineNum
				# multi line(C, java, etc), script, latex, (C, java, etc)
				m = re.search(settingRegex, line)
				if not m is None:
					try:
						postfix = m.group(1).strip()
						if postfix == ".regex":
								assertRegex = re.compile(m.group(2).strip())
						elif postfix == "":
							assertStrs = [r.strip() for r in m.group(2).split(",")]
							if len(assertStrs) == 1:
								assertRegex = re.compile(assertStrs[0])
							elif len(assertStrs) >= 2:
								assertRegex = re.compile("[(?:" + ")(?:".join(assertStrs) + ")]")
					except Exception, msg:
							self.errorLineMsg[lineNum] = str(msg)
							yield lineNum
