import sys
import argparse
from workflow import Workflow, ICON_WEB, web, PasswordNotFound

def slackChannels(api_key):

    channels = web.get('https://slack.com/api/channels.list?token=' + api_key + '&count=50&pretty=1').json()
    channelsList = channels['channels']

    return channelsList

def searchSlackChannels(channels):
    elements = []
    elements.append(channels['name'])
    return u' '.join(elements)

def main(wf):

    try:
        api_key = wf.get_password('slack_api_key')
    except PasswordNotFound:
        wf.add_item('No API key set.'
            'Please run slt',
            valid = False)
        wf.send_feedback()
        return 0

    def wrapper():
        return slackChannels(api_key)

    channelsList = wf.cached_data('channels', wrapper, max_age = 180)

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    if query:
        channelsList = wf.filter(query, channelsList, key = searchSlackChannels)

    for channels in channelsList:
        if channels['is_member'] == True:
            wf.add_item(title = channels['name'],
                subtitle = 'Member',
                arg = channels['id'],
                valid = True)
        elif channels['is_member'] == False:
            wf.add_item(title = channels['name'],
                subtitle = 'Not a member',
                arg = channels['id'],
                valid = True)

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))