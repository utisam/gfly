#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class LatexErrorGenerator(ErrorGenerator):
	command = ["lacheck"]
	startFilePath = True
	parseRegex = "^.., line ([0-9]+): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = subprocess.PIPE
	stderr = None
