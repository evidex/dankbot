#!/usr/bin/env python

######################################################################
# Utility functions for the dankbot module
######################################################################

import logging
import sys
import collections

def setup_logging(name, verbose, debug):
    pass


def dict_to_default_dict(factory, data):
    """ Takes a dict of dicts and parses it into a default_dict of default_dicts
    """
    if type(data) != dict:
        return data
    result = collections.defaultdict(factory)
    for key in data.keys():
        result[key] = dict_to_default_dict(factory, data[key])
    return result
