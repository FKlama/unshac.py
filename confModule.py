#!/usr/bin/python
#
# Project Name:  unshac.py
# File:          confModule.py
# Author:        Nina Alexandra Klama
# License:       GPL v3 (see included LICENSE file)
#
# This script is supposed to unify the shell environment on several machines,
# while still allowing for individual differences on each machine
#

import os.path as path


class ConfModule:
  def __init__(self):
    self.dir    = path.expanduser("~/.unshac")

  def __call__(self, shell=None):
    return None

  def setConfDir(self, confDir):
    self.dir = confDir

  def getInitCommand(self, shell=""):
    return None
