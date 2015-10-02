#!/usr/bin/env python
#
# ANSI Color Support For WebSploit Framework On Windows
# Created By Soxfmr
# Email : sofmr@foxmail.com
#
# You should install COLORAMA module before you enable this feature
# For more information via https://pypi.python.org/pypi/colorama

from colorama import init
def enable():
    init(autoreset=True)
