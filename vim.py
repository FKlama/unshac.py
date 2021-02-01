#!/usr/bin/python
#
# Project Name:  unshac.py
# File:          vim.py
# Author:        Nina Alexandra Klama
# License:       GPL v3 (see included LICENSE file)
#
# This script is supposed to unify the shell environment on several machines,
# while still allowing for individual differences on each machine
#

import os.path as path

from confModule import ConfModule


class VimFile(ConfModule):
  def __init__(self, fileModule, withGvimRC=False):
    self.fileModule = fileModule
    self.gvimrc     = withGvimRC
    self.lines      = []

  def __call__(self, shell=None):
    self.fileModule.addFileList(path.join(self.dir, ".vimrc"), self.lines, '"')
    return {}

  def setVar(self, var, value=None):
    if value is None or value == True:
      self.lines.append("set " + var)
    elif value == False:
      self.lines.append("set no" + var)
    else:
      self.lines.append("set " + var + "=" + value)

  def addText(self, text):
    lines = text.splitlines()
    self.lines += lines

  def getInitCommand(self):
    out = { '.vimrc':  'echo "source ' + path.join(self.dir, '.vimrc') + '" >> ~/.vimrc'}
    if self.gvimrc:
      out += { '.gvimrc': 'echo "source ' + path.join(self.dir, '.vimrc') + '" >> ~/.gvimrc'}
    return out
