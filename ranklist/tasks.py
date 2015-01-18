# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import shared_task
import requests
import re
from ranklist.models import RankData

@shared_task
def get_naver_rank_list():
    response = requests.get('http://www.naver.com')
    rank_list = re.findall('">\d+위: (.+?)(?=</option>)', response.text)

    for i in range(10):
        rankdata = RankData()
        rankdata.word = rank_list[i]
        rankdata.site = 'naver'
        rankdata.save()

    return 'get_naver_rank_list'


@shared_task
def get_daum_rank_list():
    response = requests.get('http://www.daum.net')
    rank_list = re.findall('tabindex="-1">\n(.*)\n(?=</a>)', response.text)
    rank_list[0] = rank_list[0][8:-9]

    for i in range(10):
        rankdata = RankData()
        rankdata.word = rank_list[i]
        rankdata.site = 'daum'
        rankdata.save()

    return 'get_daum_rank_list'


@shared_task
def get_nate_rank_list():
    response = requests.get('http://www.nate.com/nate2/getlivekeyword')
    rank_list = re.findall('\[\'\d+\',\'(.+?)\'', response.text)

    for i in range(10):
        rankdata = RankData()
        rankdata.word = rank_list[i]
        rankdata.site = 'nate'
        rankdata.save()

    return 'get_nate_rank_list'

# get_nate_rank_list()
# get_naver_rank_list()
# get_daum_rank_list()