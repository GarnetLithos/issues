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
    save_model(rank_list, 'naver')

    return 'get_naver_rank_list'


@shared_task
def get_daum_rank_list():
    response = requests.get('http://www.daum.net')
    rank_list = re.findall('tabindex="-1">\n(.*)\n(?=</a>)', response.text)
    rank_list[0] = rank_list[0][8:-9]
    save_model(rank_list, 'daum')

    return 'get_daum_rank_list'


@shared_task
def get_nate_rank_list():
    response = requests.get('http://www.nate.com/nate2/getlivekeyword')
    rank_list = re.findall('\[\'\d+\',\'(.+?)\'', response.text)
    save_model(rank_list, 'nate')

    return 'get_nate_rank_list'

@shared_task
def get_zum_rank_list():
    response = requests.get('http://www.zum.com')
    rank_list = re.findall('class="d_btn_keyword" title="(.+?)">', response.text)

    save_model(rank_list, 'zum')

    return 'get_zum_rank_list'


def save_model(rank_list, site):
    for i in range(5):
        rankdata = RankData()
        rankdata.word = rank_list[i]
        rankdata.site = site
        rankdata.save()