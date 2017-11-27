from slacker import Slacker

class SlackEndpoint():
    def __init__(self, token, bot_name, channel):
        self.bot_name = bot_name
        self.channel = channel
        self.api = Slacker(token)

    def format_kill(self, km):
        """ Format a provided killmail into an object suitable to be
        passed as input to send()
        """
        raise NotImplementedError

    def send(self, data):
        payload = {
            "username": self.bot_name,
            "channel": self.channel
        }
        payload.update(data)
        print(payload)
        return self.api.chat.post_message(**payload)

    def post_km(self, km):
        return self.send(self.format_kill(km))

    def test(self):
        return self.send({"text": "Foobar2"})

if __name__ == '__main__':
    print('Tests are great, m\'kay?')
