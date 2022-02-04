#!/usr/bin/env bash

sudo apt install libffi-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.6 libgdm-dev libdb4o-cil-dev libpcap-dev libbz2-dev
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tar.xz
tar Jxfv Python-3.10.2.tar.xz
cd Python-3.10.2
./configure
sudo make # ディレクトリの python が使用可能になる
# PATH が通っている所の Python を置き変える場合
# sudo make altinstall


