#!/usr/bin/env python
#-*- coding:utf-8 -*-

from generators.CErrorGenerator import GccErrorGenerator
#from generators.CErrorGenerator import ClangErrorGenerator
from generators.CppErrorGenerator import CppErrorGenerator
from generators.CsharpErrorGenerator import CsharpErrorGenerator
from generators.DErrorGenerator import DErrorGenerator
from generators.JavaErrorGenerator import JavaErrorGenerator
from generators.JavascriptErrorGenerator import ClosureLinterErrorGenerator
#from generators.PythonErrorGenerator import PylintErrorGenerator
from generators.PythonErrorGenerator import PyflakesErrorGenerator
from generators.PerlErrorGenerator import PerlErrorGenerator
from generators.PhpErrorGenerator import PhpErrorGenerator
from generators.RubyErrorGenerator import RubyErrorGenerator
from generators.ShErrorGenerator import ShErrorGenerator
#from generators.ShErrorGenerator import BashErrorGenerator
from generators.LatexErrorGenerator import LatexErrorGenerator
""" when you want to add error generator, use under map, and add instance.
ErrorGenerator needs "errorLineMsg(Map)" and "def generateErrorLines(self, doc):"
key: language name using gedit
value: list of generator
"""
errorGenerator = {
	"C": [GccErrorGenerator()],#[ClangErrorGenerator()],
	"C++": [CppErrorGenerator()],
	"C/C++/ObjC Header": [CppErrorGenerator()],
	"C#": [CsharpErrorGenerator()],
	"D": [DErrorGenerator()],
	"Java": [JavaErrorGenerator()],
	"Javascript": [ClosureLinterErrorGenerator()],
	"Python": [PyflakesErrorGenerator()],#[PylintErrorGenerator()],
	"Perl": [PerlErrorGenerator()],
	"PHP": [PhpErrorGenerator()],
	"Ruby": [RubyErrorGenerator()],
	"sh": [ShErrorGenerator()],#[BashErrorGenerator()],
	"LaTeX": [LatexErrorGenerator()],
}

# key binding
jump_to_error_key = "<Control>1"

# notification
notification = False

