#!/usr/bin/python

import requests
from flag import flag

# <bitbar.title>Bitlink Country Clicks</bitbar.title>
# <bitbar.version>v1.0.0</bitbar.version>
# <bitbar.author>Tyler LUgger</bitbar.author>
# <bitbar.author.github>tlugger</bitbar.author.github>
# <bitbar.desc>Call the Bitly API to get click counts on bitlinks for a group within the past hour</bitbar.desc>
# <bitbar.dependencies>python,requests,emoji-country-flag</bitbar.dependencies>

# get from https://bitly.is/accesstoken
BITLY_ACCESS_TOKEN = ''

# if blank, user default GUID will be used
BITLY_GROUP_GUID = ''

def get_clicks():
    if BITLY_ACCESS_TOKEN == '':
        print "ACCESS TOKEN REQUIRED"
        exit

    group_guid = BITLY_GROUP_GUID
    if group_guid == '':
        group_guid = get_default_group()

    click_data = get_group_clicks(group_guid)

    total = 0
    additional_metrics = []
    for metric in click_data.get('metrics', []):
        total += metric['clicks']
        icon = flag(metric['value']).encode('utf-8')
        additional_metrics.append("{} {} {}".format(icon, metric['clicks'], plural_or_singular(metric['clicks'])))
    
    print "{} {}".format(total, plural_or_singular(total))

    for metric in additional_metrics:
        print "---"
        print metric
       

def plural_or_singular(count):
    if count == 1:
        return "Click"
    return "Clicks"

def get_group_clicks(group_guid):
    url = "https://api-ssl.bitly.com/v4/groups/{}/countries?unit=hour&units=1".format(group_guid)
    return make_request(url)

def get_default_group():
    url = "https://api-ssl.bitly.com/v4/user"
    user = make_request(url)
    return user.get('default_group_guid')

def make_request(url):
    resp = requests.get(url, headers={"Authorization": "Bearer {}".format(BITLY_ACCESS_TOKEN)})
    if resp.status_code != 200:
        print "Bitly Request Failed"
        exit
    return resp.json()

get_clicks()