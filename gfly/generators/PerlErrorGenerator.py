#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class PerlErrorGenerator(ErrorGenerator):
	command = ["perl", "-wc"]
	startFilePath = False
	parseRegex = "(.*) line ([0-9]+)\.$"
	lineIndex = 2
	messageIndex = 1
	stdout = None
	stderr = subprocess.PIPE
