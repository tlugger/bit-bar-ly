#!/usr/bin/python

import requests
import sys
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

CLICK_ICON = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAdCAYAAACwuqxLAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAJAAAAABAAAAkAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAGKADAAQAAAABAAAAHQAAAAA47RtIAAAACXBIWXMAABYlAAAWJQFJUiTwAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgpMwidZAAAFjElEQVRIDY1WWUhcVxg+M87muO/7Mq51q2vVoqAPcaiNPogI9cFQpZsPQihETU3J1OYh0NDSh5b61NIWBG1NU0yMUBDy0EjQYoWqVaEiOg2ujTNuM86cfv/x3st1S3Lgcs/5///86/f/9zJ2cvnIx/Ly8kvJycmjKSkpntzcXI79UzxfNjc3R0kyiqx850VvrSyQk5PTFR0dzfE4dDrdHdA7QkNDh6Kionh8fPx2XV1dviT70kY0uCAMlJSUvEXKk5KSvpcNdnd3h9C+vr4+EYZ2ExMTtzo7OwMkvuKYLH/eW3his9kMCQkJdng6TUJ5eXm1YWFhm1qtljx/PDY2pmtqarIEBARwRHlLUqQ/T+FpmvCiuLi4ktIAxW+2trZG0D44ONiF3N8PCgriFovld7oYFxf3AFHOSkoo+gsXKVYEnE5nktfrZenp6dMjIyOXaY8iv7G0tHQZBr7b3t5+nTRxzv/d399/ZWBggCLniPzCNOlIAI8wotFonuEyW19fj9zc3NRDKTMajcvgs62trcXDw0PaBgUGBj7CUzgzMyPuwYCXGM9bogbV1dXxCN2LFFzF+wrSw/Pz8wuli7f0ev1+S0uLn1pRbW2tMS0tzYi75OyFSwkxOzv7WyDocz8/vysoMC8qKnpVumUzGAxegGAUSJqA3M1ztJ0xIhMoRDLihec2hB8yPDxsNZlMIiekCEhyYWmQOqvZbObz8/PFBQUFkXDmq8XFxdLMzMzfhoaGViBKOo/wUFbOpE6JxN/f/wYiOASi8iBI6zqi4oWFhS10ALJG0ISEMqohDw8PP0SaLhFPKj5tj5sLbyqWjCYDMYAgUXwUXab7ejwet8PheCjxR46OjhgM/IpR8pHb7dbNzs7+kJqa+qCtrW0dtK9RfDPJygpoT0ukDWnoQQQuVQ16gTKXr69vIgkBYT3wmre3t4suz8rKugEyB/1ZZGTkXyEhIRwQ/4ZSQp6yjo4OI3UytpQ/yrnAOPJOR3lxGBDyREDRGaISCFxZWfGg+AyGrGtraznomWEYe1vkHFC8PTg4aO/r67PL6Njb29uHxyIaUgaDRh8fHwMKLyJGSpA9zjA2iM0QsRnO7I2Pj/8jCIxNIgKjDkiwzc3NdaGoc1Cwu7q6arNYLN6DgwMnGstLXtLKyMiYQs5/AcocdrudvDfCAUbIIj4i8WBPDpvojGWmGul2dnY+hPKJjY2N14iKpvlkeXm5F8b+A2rsaC6RMjjRD3Y/ICkUAp6LiPJv1MlB94AoE7rehHtejBEieckBLTyhGNeIgqWFgptAQie8D4YCP+R875jFjMSX9mxqaurHmpqaEtTtgGgRERGTMTEx99EPTknGQymkwfYZVbysrOyqxBDjF/C/jRHtwljOJjqNA7xOI45YilE6YImi421raGjg2oWFhWsIbRAp+AJK3wfDTVLT09PXofQaPBMKYMwDsoIgeK7FeCdnTnerbIBRipSFwg5Qp+L9rkQUikmRIvT8jUYaeMeoYOwO0LnLkAKZwADRn6j1KyoqKBJa5OHLGhAXpDuU+j4U3C6IaiOA7V1MTF5ZWfmedMOAz6QStqzlvLcUrZBFNw/i2z2vllMigYGf6btbWlr6jiSgf9G8Jzm1I7GxsX/AwKjawIl0oahDGNscsGuThHQwIjfRiXvyAZ0bRHur1ZoAyHKkqUfmKW91uqD8HkYD/QTINSE5SgFB9vQj4E0CQN89MkC/OXQ+s9RGoPwuFR7N19/Y2JhyRlhFID6+Ew9pyuK70U4sFVBVktgSxicnJ0VPQPhjTMteDDgaCQuYa39izmAk2Z1IZQA6Ng7nfHR/KnqKoYYfTExM9J3UeM5JXTSEa0Fkn+KH4Ak6fwNDz11VVcXx7+TCmH4KQ4/A78KdaJUq7f8cwvLy17IF/wAAAABJRU5ErkJggg=="

def get_clicks():
    if BITLY_ACCESS_TOKEN == '':
        print "Missing Access Token"
        sys.exit(0)

    group_guid = BITLY_GROUP_GUID
    if group_guid == '':
        group_guid = get_default_group()

    click_data = get_group_countries(group_guid)
    city_data = get_group_cities(group_guid)

    total = 0
    additional_metrics = {}
    for metric in click_data.get('metrics', []):
        total += metric['clicks']
        icon = flag(metric['value']).encode('utf-8')
        additional_metrics[metric['value']] = "{} {} {}".format(icon, metric['clicks'], plural_or_singular(metric['clicks']))
    
    print "{} | templateImage={}".format(total, CLICK_ICON)

    for country, metric in additional_metrics.items():
        print "---"
        print metric
        for city_metric in city_data.get('metrics', []):
            if city_metric['country'] == country:
                print "- {}: {}".format(city_metric['city'], city_metric['clicks'])
       

def plural_or_singular(count):
    if count == 1:
        return "Click"
    return "Clicks"

def get_group_countries(group_guid):
    return _get_group_clicks(group_guid, "countries")

def get_group_cities(group_guid):
    return _get_group_clicks(group_guid, "cities")

def _get_group_clicks(group_guid, facet):
    url = "https://api-ssl.bitly.com/v4/groups/{0}/{1}?unit=day&units=1".format(group_guid, facet)
    return make_request(url)

def get_default_group():
    url = "https://api-ssl.bitly.com/v4/user"
    user = make_request(url)
    return user.get('default_group_guid')

def make_request(url):
    resp = requests.get(url, headers={"Authorization": "Bearer {}".format(BITLY_ACCESS_TOKEN)})
    if resp.status_code != 200:
        print "Bitly Request Failed"
        sys.exit(0)
    return resp.json()

get_clicks()