#!/usr/bin/env python3

# Copyright (c) 2020, Suzuki Taisei.
# All rights reserved.
#
# $Id: pman.py,v 1.32 2022/02/01 07:50:31 suzuki

import urllib.request
from bs4 import BeautifulSoup
import time
import argparse
import requests
import subprocess

murl = "https://docs.python.org/ja/3/library/"
furl = "https://docs.python.org/ja/3/library/functions.html"


def option_parser():
    parser = argparse.ArgumentParser(description="choose python module")
    parser.add_argument(
        '-m', '--module', type=str, help='choose python module')
    parser.add_argument(
        '-f', '--function', action="store_true",  help='choose python function')
    option = parser.parse_args()
    return option


def html_parser(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    # response = requests.get(url)
    # response.encoding = response.apparent_encoding
    # html = response.text
    soup = BeautifulSoup(html, "lxml")
    print(soup.get_text().strip())


def main():
    opt = option_parser()
    if(opt.module):
        url_behind = opt.module + ".html"
        url = murl + url_behind
        html_parser(url)
    elif(opt.function):
        html_parser(furl)


main()
