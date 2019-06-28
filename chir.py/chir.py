#!/usr/bin/env python
# Chir.py Twitter Bot - Developed by acidvegas in Python (https://acid.vegas/chir.py)
# chir.py

import sys

sys.dont_write_bytecode = True

import debug

debug.info()
if not debug.check_version(3):
    debug.error_exit('Chir.py requires Python version 3 to run!')
if not debug.get_windows():
    if debug.check_root():
        debug.error_exit('Do not run Chir.py as root!')
debug.check_imports()
debug.check_config()
import twitter
twitter.login()
twitter.main_loop()
debug.keep_alive()