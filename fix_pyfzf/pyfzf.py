#!/usr/bin/env python
# coding: utf-8


# imports
from plumbum import local, FG
import tempfile
import os
import sys

# constants
FZF_URL = "https://github.com/junegunn/fzf"
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

#VERSION = open(CURRENT_DIR+'/VERSION').read().strip('\n').split('.')


class FzfPrompt:

    def __init__(self):
        self.sh = local['sh']

        # check fzf
        try:
            self.fzf = local['fzf']
        except:
            raise SystemError(
                "Cannot find 'fzf' installed on PATH. ( {0} )".format(FZF_URL))

    def prompt(self, choices=None, fzf_options=""):

        # convert lists to strings [ 1, 2, 3 ] => "1\n2\n3"
        choices_str = '\n'.join(map(str, choices))

        selection = []

        with tempfile.NamedTemporaryFile() as input_file:
            with tempfile.NamedTemporaryFile() as output_file:

                # create an temp file with list entries as lines
                input_file.write(choices_str.encode())
                input_file.flush()

                self.sh['-c', CURRENT_DIR+"/filefzf.sh {0} {1} {2}".format(
                    input_file.name, output_file.name, fzf_options)] & FG

                # get selected options
                with open(output_file.name) as f:
                    for line in f:
                        selection.append(line.strip('\n'))

        return selection
