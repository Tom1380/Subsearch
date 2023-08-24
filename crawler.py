#!/usr/bin/python3

from pytrends.request import TrendReq
import requests
import time
from datetime import datetime

pytrend = TrendReq()


def get_trending_searches_for_country(pn):

    df = pytrend.realtime_trending_searches(pn=pn, count=1000)

    keywords = set()

    for entities in df['entityNames']:
        keywords.update(entities)

    return keywords


def get_trending_searches():
    f = get_trending_searches_for_country
    return f('GB') | f('AU') | f('US')


while True:
    trending_searches = get_trending_searches()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'{len(trending_searches)} queries at {current_time}')

    for ts in trending_searches:
        requests.post(
            f'http://localhost:2000/request_download/ytsearch5:{ts}'
        )

    # An hour
    time.sleep(60 * 60)