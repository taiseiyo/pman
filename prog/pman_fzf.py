#!/usr/bin/env python3

# Copyright (c) 2020, Suzuki Taisei.
# All rights reserved.
#
# $Id: pman.py,v 1.32 2022/02/01 07:50:31 suzuki

import urllib.request
from bs4 import BeautifulSoup
import time
import argparse
import subprocess
from pyfzf.pyfzf import FzfPrompt

murl = "https://docs.python.org/ja/3/library/"
furl = "https://docs.python.org/ja/3/library/functions.html"


def option_parser():
    parser = argparse.ArgumentParser(description="choose python module")
    parser.add_argument(
        '-m', '--module', action="store_true", help='flag for python module')
    parser.add_argument(
        '-f', '--function', action="store_true",  help='flag for python function')
    option = parser.parse_args()
    return option


def html_parser(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
    except urllib.error.HTTPError:
        print("公式に参照できるページがありません")
        exit()
    return BeautifulSoup(html, "lxml")


def fzf_search():
    module_list_url = "https://docs.python.org/3/py-modindex.html"
    soup = html_parser(module_list_url)
    module_list = [sp.get_text()
                   for sp in soup.find_all("code", class_="xref")]
    fzf = FzfPrompt()
    url_behind = fzf.prompt(module_list)[0]
    return murl + url_behind + ".html"


def main():
    opt = option_parser()
    if(opt.module):
        url = fzf_search()
        soup = html_parser(url)
        print(soup.get_text())
    elif(opt.function):
        html_parser(furl)


main()
