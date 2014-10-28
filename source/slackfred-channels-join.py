import sys
import argparse
from workflow import Workflow, ICON_WEB, web, PasswordNotFound

def getChannelName(api_key, query):
    channelsList = web.get('https://slack.com/api/channels.list?token=' + api_key + '&pretty=1').json()

    for channels in channelsList['channels']:
        if channels['id'] == query:
            channelName = channels['name']
    return channelName

def main(wf):

    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?', default = None)
    args = parser.parse_args(wf.args)

    try:
        api_key = wf.get_password('slack_api_key')
    except PasswordNotFound:
        wf.add_item('No API key set.'
            'Please run slt',
            valid = False)
        wf.send_feedback()
        return 0

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    channelName = getChannelName(api_key, query)

    web.get('https://slack.com/api/channels.join?token=' + api_key + '&name=' + channelName + '&pretty=1')

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))