#!/usr/bin/python
#
# Project Name:  unshac.py
# File:          alias.py
# Author:        Frederik Klama
# License:       GPL v3 (see included LICENSE file)
#
# This script is supposed to unify the shell environment on several machines,
# while still allowing for individual differences on each machine
#

import os.path as path

from confModule import ConfModule


def _bash(alias, cmd):
  return "alias " + alias + '"' + cmd + '"'


class Alias(ConfModule):
  def __init__(self, shell):
    self.shell        = shell
    self.aliasList    = []
    self.shellMap     = { 'bash':     _bash
                        , 'zsh':      _bash
                        }
    self.shellFile    = { 'bash':       ".bashrc"
                        , 'zsh':        ".zshrc"
                        }[shell]

  def __call__(self):
    outList = []
    for alias in self.aliasList:
      outList.append(self.shellMap[self.shell](alias['alias'], alias['cmd']))
    filename = path.join(self.dir, self.shellFile)
    return {filename: outList}

  def addAlias(self, alias, cmd):
    self.aliasList.append({'alias': alias, 'cmd':cmd})

  def getInitCommand(self):
    out  = 'echo "source '
    out += path.join(self.dir, self.shellFile)
    out += '" >> ~/' + self.shellFile
    return {self.shellFile: out}
