#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
import os

# LANG=ja_JP.UTF-8
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append('../gfly')


def TestCErrorGenerator():
	from CErrorGenerator import CErrorGenerator
	gen = CErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.c')]
	assert len(lines) == 1
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == "error: expected ‘;’ before ‘return’"


def TestCppErrorGenerator():
	from CppErrorGenerator import CppErrorGenerator
	gen = CppErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.cpp')]
	assert len(lines) == 1
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == "error: ‘cout’ was not declared in this scope"


def TestCsharpErrorGenerator():
	from CsharpErrorGenerator import CsharpErrorGenerator
	gen = CsharpErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.cs')]
	assert len(lines) == 2
	assert lines[0] == 6
	assert gen.errorLineMsg[lines[0]] == "error CS1525: Unexpected symbol `}'"
	assert lines[1] == 8
	assert gen.errorLineMsg[lines[1]] == 'error CS8025: Parsing error'


def TestJavaErrorGenerator():
	from JavaErrorGenerator import JavaErrorGenerator
	gen = JavaErrorGenerator()
	lines = [x for x in gen.generateErrorLines('MockSrc.java')]
	assert len(lines) == 1
	assert lines[0] == 3
	assert gen.errorLineMsg[lines[0]] == "';' がありません。"


def TestClosureLinterErrorGenerator():
	from JavascriptErrorGenerator import ClosureLinterErrorGenerator
	gen = ClosureLinterErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.js')]
	assert len(lines) == 1
	assert lines[0] == 1
	assert gen.errorLineMsg[lines[0]] == '(New error) Missing semicolon at end of line'


def TestPylintErrorGenerator():
	from PythonErrorGenerator import PylintErrorGenerator
	gen = PylintErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.py')]
	assert len(lines) == 1
	assert lines[0] == 8
	assert gen.errorLineMsg[lines[0]] == 'invalid syntax'


def TestPyflakesErrorGenerator():
	from PythonErrorGenerator import PyflakesErrorGenerator
	gen = PyflakesErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.py')]
	assert len(lines) == 1
	assert lines[0] == 8
	assert gen.errorLineMsg[lines[0]] == 'invalid syntax'


def TestPerlErrorGenerator():
	from PerlErrorGenerator import PerlErrorGenerator
	gen = PerlErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.pl')]
	assert len(lines) == 1
	assert lines[0] == 1
	assert gen.errorLineMsg[lines[0]] == 'Can\'t find string terminator \'"\' anywhere before EOF at mocksrc.pl'


def TestPhpErrorGenerator():
	from PhpErrorGenerator import PhpErrorGenerator
	gen = PhpErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.php')]
	assert len(lines) == 1
	assert lines[0] == 2
	assert gen.errorLineMsg[lines[0]] == 'syntax error, unexpected T_ENCAPSED_AND_WHITESPACE in mocksrc.php'


def TestRubyErrorGenerator():
	from RubyErrorGenerator import RubyErrorGenerator
	gen = RubyErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.rb')]
	assert len(lines) == 1
	assert lines[0] == 1
	assert gen.errorLineMsg[lines[0]] == 'unterminated string meets end of file'


def TestShErrorGenerator():
	from ShErrorGenerator import ShErrorGenerator
	gen = ShErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.sh')]
	assert len(lines) == 1
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == 'Syntax error: "fi" unexpected (expecting "then")'


def TestBashErrorGenerator():
	from ShErrorGenerator import BashErrorGenerator
	gen = BashErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.sh')]
	assert len(lines) == 1
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == "期待してない token `fi' のあたりにシンタックスエラー"

def TestLatexErrorGenerator():
	from LatexErrorGenerator import LatexErrorGenerator
	gen = LatexErrorGenerator()
	lines = [x for x in gen.generateErrorLines('mocksrc.tex')]
	assert len(lines) == 2
	assert lines[0] == 4
	assert gen.errorLineMsg[lines[0]] == 'possible unwanted space at "{"'
	assert lines[1] == 14
	assert gen.errorLineMsg[lines[1]] == '{argument} missing for \\begin'

