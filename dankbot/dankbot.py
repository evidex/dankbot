#!/usr/bin/env python

from utils import *

import argparse

class Dankbot:
    def __init__(self, verbose=True, debug=False):
        self.logger = setup_logger(self.__name__, verbose, debug)

    def run(self):
        done = False
        while not done:
            km = self.kb.fetch_killmail()
            km = filter_km(km, config)
            if km:
                for endpoint in self.endpoints:
                    endpoint.post_km(km)
        # Tidy up exit out here

if __name__ == '__main__':
    # Setup parser

    pass

