#-*- coding:utf-8 -*-
import subprocess
from ErrorGenerator import ErrorGenerator

class GccErrorGenerator(ErrorGenerator):
	command = ["gcc", "-Wall", "-fsyntax-only"]
	startFilePath = True
	parseRegex = "^:([0-9]+): (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE

class ClangErrorGenerator(ErrorGenerator):
	command = ["clang", "-Wall", "-fsyntax-only"]
	startFilePath = True
	parseRegex = "^:([0-9]+):[0-9]+: (.*)"
	lineIndex = 1
	messageIndex = 2
	stdout = None
	stderr = subprocess.PIPE
