# -*- coding: utf-8 -*-
"""Main module."""
import os
import re
import subprocess

if 'MODULE_VERSION' not in os.environ:
    os.environ['MODULE_VERSION_STACK'] = '3.2.10'
    os.environ['MODULE_VERSION'] = '3.2.10'
else:
    os.environ['MODULE_VERSION_STACK'] = os.environ['MODULE_VERSION']
os.environ[
    'MODULESHOME'] = '/cm/local/apps/environment-modules/3.2.10/Modules/3.2.10'

if 'MODULEPATH' not in os.environ:
    f = open(os.environ['MODULESHOME'] + "/init/.modulespath", "r")
    path = []
    for line in f.readlines():
        line = re.sub("#.*$", '', line)
        if line is not '':
            path.append(line)
    os.environ['MODULEPATH'] = ':'.join(path)

if 'LOADEDMODULES' not in os.environ:
    os.environ['LOADEDMODULES'] = ''


def module(*args: str) -> str:
    """Manages modules at CSCS.

       Module is a user interface to the Modules package. The Modules package
       provides for the dynamic modification of the user's environment and make
       applications and libraries available to the user.

       Args:
           *args: A sequence of strings. The elements of the sequence correspond
                  to the commandline arguments of the command module (see
                  man module).

       Returns:
           A string containing the output of the module command.
    """
    if isinstance(args[0], list):
        args = args[0]
    else:
        args = list(args)
    (output, error) = subprocess.Popen(
        [
            '/cm/local/apps/environment-modules/3.2.10/Modules/%s/bin/modulecmd'
            % os.environ['MODULE_VERSION'], 'python'
        ] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8").communicate()
    exec(output)
    return error
