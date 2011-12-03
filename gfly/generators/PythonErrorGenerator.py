#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class PylintErrorGenerator(ErrorGenerator):
	command = ["pylint", "-E"]
	startFilePath = False
	parseRegex = "^E: *([0-9]*): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = subprocess.PIPE
	stderr = None

class PyflakesErrorGenerator(ErrorGenerator):
	command = ["pyflakes"]
	startFilePath = True
	parseRegex = "^:([0-9]*): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = subprocess.PIPE
	stderr = subprocess.PIPE
