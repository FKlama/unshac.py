#!/usr/bin/python
#
# Project Name:  unshac.py
# File:          env.py
# Author:        Frederik Klama
# License:       GPL v3 (see included LICENSE file)
#
# This script is supposed to unify the shell environment on several machines,
# while still allowing for individual differences on each machine
#

import os
import copy
import os.path as path

from confModule import ConfModule


def _bash(varName, value):
  return "export " + varName + "=" + value


class Environment(ConfModule):
  def __init__(self, shell):
    self.shell        = shell
    self.preVariables = os.environ
    self.var          = copy.deepcopy(self.preVariables)
    self.shellMap     = { 'bash':       _bash
                        , 'zsh':        _bash
                        }
    self.shellFile    = { 'bash':       ".bashrc"
                        , 'zsh':        ".zshrc"
                        }[shell]

  def __call__(self):
    outLines = []
    for v in self.var:
      if v in self.preVariables:
        if self.var[v] == self.preVariables[v]:
          continue
      outLines.append(self.shellMap[self.shell](v, self.var[v]))
    filename = path.join(self.dir, self.shellFile)
    return {filename: outLines}

  def preList(self):
    return self.preVariables.keys()

  def preEnv(self):
    return self.preVariables

  def setEnv(self, varName, value):
    self.var[varName] = value

  def getPathList(self, varName):
    if varName not in self.var:
      return None
    pathList = self.var[varName].split(":")
    return pathList

  def setVarFromList(self, varName, varList):
    self.var[varName] = ":".join(varList)

  def getInitCommand(self):
    out  = 'echo "source '
    out += path.join(self.dir, self.shellFile)
    out += '" >> ~/' + self.shellFile
    return {self.shellFile: out}
