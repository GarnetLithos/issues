# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ranklist.models import RankData
from django.db.models import Count


def bullets1(request):
    return render(request, 'ranklist/bullets/bullets1.html', )


def bullets2(request):
    return render(request, 'ranklist/bullets/bullets2.html', )


def sort_bar_chart(request):
    return render(request, 'ranklist/sortableBarChart/sortBarChart.html', )


def base(request):
    return render(request, 'ranklist/base.html', )


def hours(request):
    time = datetime.datetime.now()
    return render(request, 'ranklist/hours.html', {'time': time, 'hours': reversed(range(0, time.hour + 1))})


def days(request):
    time = datetime.datetime.now()
    weekday_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    weekday = []
    start = time.weekday()
    for i in range(time.day):
        weekday.append(weekday_list[start])
        start -= 1
        if start == -1:
            start = 6

    weekday.reverse()
    context = {
        'time': time,
        'days': reversed(range(1, time.day + 1)),
        'weekday': weekday,
    }
    return render(request, 'ranklist/days.html', context)


def months(request):
    time = datetime.datetime.now()
    return render(request, 'ranklist/months.html', {'time': time, 'months': reversed(range(1, time.month + 1))})


def years(request):
    time = datetime.datetime.now()
    return render(request, 'ranklist/years.html', {'time': time, 'years': reversed(range(2014, time.year + 1))})


@api_view(['GET'])
def year_data(request, site, year):
    rankdata = RankData.objects.filter(time__year=year)
    contents = create_contents(rankdata)

    return Response(contents)


@api_view(['GET'])
def month_data(request, site, year, month):
    start_date = datetime.date(int(year), int(month), 1)
    end_date = datetime.date(int(year), int(month) + 1, 1)
    rankdata = RankData.objects.filter(time__range=(start_date, end_date))
    contents = create_contents(rankdata)

    return Response(contents)


@api_view(['GET'])
def day_data(request, site, year, month, day):
    start_date = datetime.date(int(year), int(month), int(day))
    end_date = start_date + datetime.timedelta(days=1)
    rankdata = RankData.objects.filter(time__range=(start_date, end_date))
    contents = create_contents(rankdata)

    return Response(contents)


@api_view(['GET'])
def hour_data(request, site, year, month, day, hour):
    start_date = datetime.date(int(year), int(month), int(day))
    end_date = start_date + datetime.timedelta(days=1)
    rankdata = RankData.objects.filter(time__range=(start_date, end_date), time__hour=hour)
    # rankdata = RankData.objects.filter(time__year=year).filter(time__month=month).filter(time__day=day).filter(time__hour=hour)
    contents = create_contents(rankdata)

    return Response(contents)


def create_contents(rankdata):
    rankdata_all = rankdata.values('word').annotate(count=Count('word')).order_by('-count')
    rankdata_exclude_nate = rankdata_all[:].exclude(site='nate')
    rankdata_exclude_nate_daum = rankdata_exclude_nate[:].exclude(site='daum')
    rank_data_list = []
    rank_data_list.append(rankdata_exclude_nate)
    rank_data_list.append(rankdata_exclude_nate_daum)
    contents = []

    for rankdata in rankdata_all:
        line_data = {}
        line_data['title'] = rankdata['word']
        line_data['subtitle'] = 'count'
        line_data['ranges'] = [0, rankdata_all[0]['count'], rankdata_all[0]['count']]
        line_data['measures'] = [rankdata['count']]

        for measure_data_list in rank_data_list:
            measure = 0
            for measure_data in measure_data_list:
                if measure_data['word'] == line_data['title']:
                    measure = measure_data['count']
                    # do add pop measure data

                    break

            line_data['measures'].append(measure)

        line_data['markers'] = [rankdata_all[0]['count']]
        contents.append(line_data)

    return contents