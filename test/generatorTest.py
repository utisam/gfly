#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from nose.tools import eq_

# LANG=ja_JP.UTF-8
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, '../gfly/generators'))


def TestGccErrorGenerator():
	from CErrorGenerator import GccErrorGenerator
	gen = GccErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.c'))]
	# gcc version 4.6.1 (Ubuntu/Linaro 4.6.1-9ubuntu3)
	eq_(len(lines), 1)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], "2: error: expected ‘;’ before ‘return’")

def TestClangErrorGenerator():
	from CErrorGenerator import ClangErrorGenerator
	gen = ClangErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.c'))]
	# clang version 2.9 (tags/RELEASE_29/final)
	eq_(len(lines), 1)
	eq_(lines[0], 3)
	eq_(gen.errorLineMsg[lines[0]], "error: expected ';' after expression")

def TestCppErrorGenerator():
	from CppErrorGenerator import CppErrorGenerator
	gen = CppErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.cpp'))]
	# gcc version 4.6.1 (Ubuntu/Linaro 4.6.1-9ubuntu3)
	eq_(len(lines), 1)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], "2: error: ‘cout’ was not declared in this scope")


def TestCsharpErrorGenerator():
	from CsharpErrorGenerator import CsharpErrorGenerator
	gen = CsharpErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.cs'))]
	# Mono C# compiler version 2.10.5.0
	eq_(len(lines), 1)
	eq_(lines[0], 6)
	eq_(gen.errorLineMsg[lines[0]], "error CS1525: Unexpected symbol `}', expecting `;'")


def TestDErrorGenerator():
	from DErrorGenerator import DErrorGenerator
	gen = DErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.d'))]
	# gcc version 4.4.6 (Ubuntu/Linaro 4.4.6-7)
	eq_(len(lines), 1)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], "found 'return' when expecting ';' following statement")


def TestJavaErrorGenerator():
	from JavaErrorGenerator import JavaErrorGenerator
	gen = JavaErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'MockSrc.java'))]
	eq_(len(lines), 1)
	eq_(lines[0], 3)
	eq_(gen.errorLineMsg[lines[0]], "';' がありません。")


def TestClosureLinterErrorGenerator():
	from JavascriptErrorGenerator import ClosureLinterErrorGenerator
	gen = ClosureLinterErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.js'))]
	eq_(len(lines), 1)
	eq_(lines[0], 1)
	eq_(gen.errorLineMsg[lines[0]], '(New error) Missing semicolon at end of line')


def TestPylintErrorGenerator():
	from PythonErrorGenerator import PylintErrorGenerator
	gen = PylintErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.py'))]
	eq_(len(lines), 1)
	eq_(lines[0], 8)
	eq_(gen.errorLineMsg[lines[0]], 'invalid syntax')


def TestPyflakesErrorGenerator():
	from PythonErrorGenerator import PyflakesErrorGenerator
	gen = PyflakesErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.py'))]
	eq_(len(lines), 1)
	eq_(lines[0], 8)
	eq_(gen.errorLineMsg[lines[0]], 'invalid syntax')


def TestPerlErrorGenerator():
	from PerlErrorGenerator import PerlErrorGenerator
	gen = PerlErrorGenerator()
	filepath = os.path.join(BASE_DIR, 'mocksrc.pl')
	lines = [x for x in gen.generateErrorLines(filepath)]
	eq_(len(lines), 1)
	eq_(lines[0], 1)
	eq_(gen.errorLineMsg[lines[0]], 'Can\'t find string terminator \'"\' anywhere before EOF at ' + filepath)


def TestPhpErrorGenerator():
	from PhpErrorGenerator import PhpErrorGenerator
	gen = PhpErrorGenerator()
	filepath = os.path.join(BASE_DIR, 'mocksrc.php')
	lines = [x for x in gen.generateErrorLines(filepath)]
	eq_(len(lines), 1)
	eq_(lines[0], 2)
	eq_(gen.errorLineMsg[lines[0]], 'syntax error, unexpected T_ENCAPSED_AND_WHITESPACE in ' + filepath)


def TestRubyErrorGenerator():
	from RubyErrorGenerator import RubyErrorGenerator
	gen = RubyErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.rb'))]
	eq_(len(lines), 1)
	eq_(lines[0], 1)
	eq_(gen.errorLineMsg[lines[0]], 'unterminated string meets end of file')


def TestShErrorGenerator():
	from ShErrorGenerator import ShErrorGenerator
	gen = ShErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.sh'))]
	eq_(len(lines), 1)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], 'Syntax error: "fi" unexpected (expecting "then")')


def TestBashErrorGenerator():
	from ShErrorGenerator import BashErrorGenerator
	gen = BashErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.sh'))]
	# GNU bash, version 4.2.10(1)-release (x86_64-pc-linux-gnu)
	eq_(len(lines), 1)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], "syntax error near unexpected token `fi'")

def TestTextErrorGenerator():
	from TextErrorGenerator import TextErrorGenerator
	gen = TextErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.txt'))]
	eq_(tuple(lines), (2, 4, 5))
	eq_(gen.errorLineMsg[lines[0]], "hit!")
	eq_(gen.errorLineMsg[lines[1]], "hit!")
	eq_(gen.errorLineMsg[lines[2]], "unexpected end of regular expression")

def TestLatexErrorGenerator():
	from LatexErrorGenerator import LatexErrorGenerator
	gen = LatexErrorGenerator()
	lines = [x for x in gen.generateErrorLines(os.path.join(BASE_DIR, 'mocksrc.tex'))]
	eq_(len(lines), 2)
	eq_(lines[0], 4)
	eq_(gen.errorLineMsg[lines[0]], 'possible unwanted space at "{"')
	eq_(lines[1], 14)
	eq_(gen.errorLineMsg[lines[1]], '{argument} missing for \\begin')

