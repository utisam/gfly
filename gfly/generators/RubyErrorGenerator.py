#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class RubyErrorGenerator(ErrorGenerator):
	command = ["ruby", "-c"]
	startFilePath = True
	parseRegex = "^:([0-9]+): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE
