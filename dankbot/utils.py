#!/usr/bin/env python

######################################################################
# Utility functions for the dankbot module
######################################################################

import logging
import sys
import collections

import esipy

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

class esi():
    """ Trivial wrapper around the esipy module
    """

    ESI_SWAGGER_URI="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility"
    def __init__(self, app, client):
        self.app = esipy.App(url=ESI_SWAGGER_URI)
        self.client = esipy.EsiClient(retry_requests=True)
