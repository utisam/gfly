#-*- coding:utf-8 -*-
import re
import subprocess

class ErrorGenerator:
	""" abstract ErrorGenerator
	you must define:
		'command', 'startFilePath', 'parseRegex',
		'lineIndex', 'messageIndex'
	"""
	errorLineMsg = {}
	def generateErrorLines(self, filepath):
		"""generate error lines
		"""
		ps = subprocess.Popen(self.command + [filepath], stdout=self.stdout, stderr=self.stderr)
		self.errorLineMsg.clear()
		if self.startFilePath:
			length = len(filepath)
		else:
			length = 0
		try:
			if self.stdout:
				for l in self.parse(ps.stdout, length):
					yield l
			if self.stderr:
				for l in self.parse(ps.stderr, length):
					yield l
		finally:
			if self.stdout:
				ps.stdout.close()
			if self.stderr:
				ps.stderr.close()
	def parse(self, stream, length):
		for line in stream:
			matchObj = re.search(self.parseRegex, line[length:])
			if not matchObj is None:
				errorLine = int(matchObj.group(self.lineIndex))
				if not self.errorLineMsg.has_key(errorLine):
					self.errorLineMsg[errorLine] = matchObj.group(self.messageIndex).strip()
					yield errorLine
