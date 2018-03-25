import json
from pprint import pprint
import time
import requests
import sys
import collections

import utils


REDIS_URL = 'https://redisq.zkillboard.com/listen.php'
POLL_DELAY = 0.5 # Time in seconds to wait between calls to zKillboard RedisQ

class zKill():
    """ zKillboard interface class
    """

    def __init__(self, verbose=True, debug=False):
        self.log = utils.setup_logging(__name__, verbose, debug)
        self.session = requests.Session()

    def check_queue(self):
        """ Check for a queue in the zKillboard RedisQ
        """
        package = None
        try:
            r = self.session.get(REDIS_URL)
        except:
            print(sys.exc_info())
            sys.exit(1)
        if r.status_code == requests.codes.ok and r.text:
            package = json.loads(r.text)['package']
        return package

    def parse_killdata(self, payload):
        """ Do any parsing of the killmail, if required
        """
        return payload

    def fetch_killdata(self):
        """ Poll the zKillboard API for a new kills until one exists.
        """
        km = None
        while not km:
            raw_data = self.check_queue()
            if raw_data:
                km = self.parse_killdata(raw_data)
            time.sleep(POLL_DELAY)
        return km

    def is_solo_kill(self, km):
        """ Returns True if a kill is considered a 'solo' kill
        """
        return km['zkb']['solo']

    def is_awox_kill(self, km):
        """ Returns True if a kill is considered a 'awox' kill
        """
        return km['zkb']['awox']

    def is_super_kill(self, km):
        """ Returns True if a kill is considered a 'super' kill
        """
        pass

    def get_kill_type(self, km):
        """ Return the type of the killmail
        """
        pass

    def get_raw_killmail(self, killmail_url):
        """ Return the full killmail data from the ESI endpoint
        """
        return self.session.get(killmail_url).json()


if __name__ == '__main__':
    """
        Interactive testing
    """

    kb = zKill()
    km = kb.fetch_killdata()

    assert len(km) != 0
    print(km['zkb'])
    pprint(kb.get_raw_killmail(km['zkb']['href']))
