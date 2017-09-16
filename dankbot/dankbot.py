#!/usr/bin/env python

from utils import *

class Dankbot:
    def __init__(self, verbose=True, debug=False):
        self.logger = setup_logger(self.__name__, verbose, debug)
