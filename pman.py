#!/usr/bin/env python3

# Copyright (c) 2020, Suzuki Taisei.
# All rights reserved.
#
# $Id: pman.py,v 1.32 2020/03/25 07:50:31 suzuki

import urllib.request
from perlcompat import getopts
from bs4 import BeautifulSoup
import time
import argparse
import subprocess

murl = "https://docs.python.org/ja/3/library/"
furl = "https://docs.python.org/ja/3/library/functions.html"


class Python_module_manual(object):
    def __init__(self, name):
        self.url = murl + name + ".html"
        self.html = urllib.request.urlopen(self.url)

    def printer(self):
        target = BeautifulSoup(self.html.read(), "lxml")
        text_data = str("")
        for text in (target.find_all(text=True)):
            text_data = text_data + text
        print(text_data.strip())


class Python_function_manual(Python_module_manual):
    def __init__(self, name):
        self.url = furl + "#" + name
        self.html = urllib.request.urlopen(self.url)


def option_parser():
    parser = argparse.ArgumentParser(description="choose python module")
    parser.add_argument(
        '-m', '--module', help='choose python module')
    parser.add_argument(
        '-f', '--function', help='choose python function')
    option = parser.parse_args()
    return option


def main():
    opt = option_parser()
    manual = Python_module_manual(opt.module)\
        if opt.module else Python_function_manual(opt.function) if opt.function else None
    manual.printer() if opt.module or opt.function else None


main()
