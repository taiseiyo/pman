#!/usr/bin/env bash
# sudo apt install libffi-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.6 libgdm-dev libdb4o-cil-dev libpcap-dev libbz2-dev
mkdir test_install
cd test_install
wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tar.xz
tar Jxfv Python-3.10.2.tar.xz
./Python-3.10.2/configure
# ディレクトリの python が使用可能になる
sudo make
# PATH が通っている所の Python を置き変える場合
# sudo make altinstall
