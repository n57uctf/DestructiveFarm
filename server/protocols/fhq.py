import requests

from server import app
from server.models import FlagStatus, SubmitResult

# Acceptance of flag: http://{HOST}:{PORT}/flag?teamid={TEAMID}&flag={FLAG}
# Where

# {HOST} - host or ip, where jury system started
# {PORT} - scoreboard/flag port, where jury system started
# {TEAMID} - number, your unique teamid (see scoreboard)
# {FLAG} - uuid, so... it's flag from enemy server
# Example of send flag (curl):

# curl http://192.168.1.10:8080/flag?teamid=keva&flag=123e4567-e89b-12d3-a456-426655440000
# http-code responses:

# 400 - wrong parameters
# 200 - flag accept
# 403 - flag not accept (reason: old, already accepted, not found)

RESPONSES = {
    200: FlagStatus.ACCEPTED,
    403: FlagStatus.REJECTED,
}

TIMEOUT = 5


def send_flags(flags, config):
    codes = []
    for flag in flags:
        r = requests.get('http://{}:{}/flag?teamid={}&flag={}'.format(
            config['SYSTEM_URL'], config['SYSTEM_PORT'],
            config['TEAM_ID'], flag))
        codes.append((flag, r.status_code, r.text))


def submit_flags(flags, config):
    codes = send_flags(flags, config)

    unknown_responses = set()
    for item in codes:
        found_status = None
        try:
            found_status = RESPONSES[item[1]]
        except KeyError:
            unknown_responses.add(item[1])
            found_status = FlagStatus.QUEUED
            unknown_responses.add(item[1])
            app.logger.warning(
                'Unknown checksystem response: %s - %s', item[1], item[2])
        yield SubmitResult(item[0], found_status, item[1])
