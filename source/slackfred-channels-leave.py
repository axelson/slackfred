import sys
import argparse
from workflow import Workflow, ICON_WEB, web, PasswordNotFound

def main(wf):

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

    web.get('https://slack.com/api/channels.leave?token=' + api_key + '&channel=' + query + '&pretty=1')

    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))