#-*- coding:utf-8 -*-
import subprocess
import re
from ErrorGenerator import ErrorGenerator

class DErrorGenerator(ErrorGenerator):
	command = ["gdc", "-Wall", "-fsyntax-only"]
	startFilePath = True
	parseRegex = re.compile("^:([0-9]+): (.*)")
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE
