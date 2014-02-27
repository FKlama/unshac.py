#!/usr/bin/python
#
# Project Name:	 unshac.py
# File:					 unshac.py
# Author:	       Frederik Klama
# License:       GPL v3 (see included LICENSE file)
#
# This script is supposed to unify the shell environment on several machines,
# while still allowing for individual differences on each machine
#

from sys import exit
import argparse

useurllib3 = False

try:
  import urllib3
  useurllib3 = True
except:
  pass

configURL       = "http://www.fklama.de/unshac/unshacConfig.example.py"
useGPG          = True
gpg_path        = "gpg"
gpg_passphrase  = "eePhaeyeew2aev5aicaengiethee2soo"
wget_bin        = "wget"              # Only needed when urllib3 is not installed
out_script_dir  = "~/.unshac"


def httpGetFile(url, path):
  if useurllib3:
    http = urllib3.PoolManager()
    r    = http.request('GET', url)
    if r.status == 200:
      with open(path, 'wb') as of:
        of.write(r.data)
    elif r.status == 404:
      print("404:", url)
    else:
      print("Error downloading file: Status =", r.status)
      exit()
  else:
    cmd = wget_bin + " -O " + path + " " + url
    system(cmd)


def updateConfig(path):
  outfile = "unshacConfig.py"
  gpgOutfile = ""
  if useGPG:
    gpg_outfile = path.join(path, outfile)
    outfile += ".gpg"
  outfile = path.join(path, outfile)
  httpGetFile(configURL, outfile)
  if useGPG:
    cmd  = gpg_path
    cmd += " --output " + gpg_outfile
    cmd += " --passphrase " + gpg_passphrase
    cmd += " -d"
    cmd += " " + outfile
    system(cmd)


if __name__ == '__main__':
  argParser = argparse.ArgumentParser(description="unshac.py")
  argParser.add_argument('--update', '-u',
    action='store_true',
    help="Force updating the config file")
  argParser.add_argument('--init', '-I',
    action='store_true',
    help="Print commands appending necessary lines to config files.")
  args = vars(argParser.parse_args())

  scriptPath = path.realpath(__file__)
  configPath = path.join(scriptPath, "unshacConfig.py")
  unshacScript = path

  if args['update'] or not path.exists(configPath):
    updateConfig(scriptPath)

  if out_script_dir:
    out_script_dir = path.abspath(path.expanduser(out_script))
  else:
    out_script_dir = path.expanduser("~/.unshac")

  if not path.exists(out_script_dir):
    os.mkdir(out_script_dir)

  try:
    import unshacConfig
  else:
    updateConfig()
    import unshacConfig

  outlines = []
  for exe in unshacConfig.execList:
    ext.setConfDir(out_script_dir)
    ret = exe(shell)
    if ret:
      outlines += ret

  with open(out_script, 'w') as oScript:
    oScript.write("\n".join(outlines) + "\n")

  initMap  = {}
  if args['init']:
    for exe in unshacConfig.execList:
      ret = exe.getInitCommand()
      for r in ret:
        if not r in initMap:
          initMap[r] = ret[r]

    for l in initMap:
      print initMap[l]
