#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class ShErrorGenerator(ErrorGenerator):
	command = ["sh", "-n"]
	startFilePath = True
	parseRegex = "^:\s*([0-9]+): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE

class BashErrorGenerator(ErrorGenerator):
	command = ["bash", "-n"]
	startFilePath = True
	parseRegex = "([0-9]+): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE
