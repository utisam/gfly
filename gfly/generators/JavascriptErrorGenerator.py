#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class ClosureLinterErrorGenerator(ErrorGenerator):
	command = ["gjslint"]
	startFilePath = False
	parseRegex = "^Line ([0-9]+), .:\d\d\d\d: (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = subprocess.PIPE
	stderr = None
