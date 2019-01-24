import requests
import os
import argparse
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser(description='- shorten url\n-get clicks count')
parser.add_argument('-u', '-url', help='URL')
args = parser.parse_args()


BITLY_URL = 'https://api-ssl.bitly.com/v4/{}'


def get_headers(token):
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}
    return headers


def shorten_url(token, link):
    url = BITLY_URL.format('shorten')
    headers = get_headers(token)
    res = requests.post(url=url, headers=headers, json={'long_url': link})
    if res.ok:
        bitly_data = res.json()
        return bitly_data['link']


def get_clicks_count(token, link):
    url = BITLY_URL.format('bitlinks/{}/clicks/summary'.format(link))
    headers = get_headers(token)
    res = requests.get(url=url, headers=headers, json={'long_url': link})
    if res.ok:
        bitly_data = res.json()
        return bitly_data['total_clicks']


if __name__ == '__main__':
    token = os.getenv("TOKEN")
    url = args.u
    clicks_count = get_clicks_count(token, url)
    if isinstance(clicks_count, int):
        print(clicks_count)
    else:
        short_link = shorten_url(token, url)
        if short_link:
            print(short_link)
        else:
            print('bad url')

