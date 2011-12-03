#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class PhpErrorGenerator(ErrorGenerator):
	command = ["php", "-l"]
	startFilePath = False
	parseRegex = ".*:  (.*) on line ([0-9]+)$"
	lineIndex = 2
	messageIndex = 1
	stdout = None
	stderr = subprocess.PIPE

