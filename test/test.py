#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append('../gfly')


class MockDocuments:

	def __init__(self, srcName):
		self.srcPath = os.path.join(BASE_DIR, srcName)

	def get_uri_for_display(self):
		return self.srcPath


def TestCErrorGenerator():
	from CErrorGenerator import CErrorGenerator
	doc = MockDocuments('mock.c')
	gen = CErrorGenerator()
	lines = [x for x in gen.generateErrorLines(doc)]
	assert len(lines) == 1
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == "error: expected ‘;’ before ‘return’"


def TestCppErrorGenerator():
	from CppErrorGenerator import CppErrorGenerator


def TestJavaErrorGenerator():
	from JavaErrorGenerator import JavaErrorGenerator


def TestPylintErrorGenerator():
	from PythonErrorGenerator import PylintErrorGenerator

def TestPyflakesErrorGenerator():
	from PythonErrorGenerator import PyflakesErrorGenerator
	doc = MockDocuments('mock.py')
	gen = PyflakesErrorGenerator()
	lines = [x for x in gen.generateErrorLines(doc)]
	assert len(lines) == 1
	assert lines[0] == 8
	assert gen.errorLineMsg[lines[0]] == "invalid syntax"

def TestCsharpErrorGenerator():
	from CsharpErrorGenerator import CsharpErrorGenerator


def TestPerlErrorGenerator():
	from PerlErrorGenerator import PerlErrorGenerator


def TestPhpErrorGenerator():
	from PhpErrorGenerator import PhpErrorGenerator


def TestShErrorGenerator():
	from ShErrorGenerator import ShErrorGenerator

