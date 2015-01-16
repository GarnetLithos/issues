from django.http import HttpResponse
from django.shortcuts import render
import datetime
from ranklist.models import RankData


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


def year_data(request, site, year):
    return HttpResponse("year_data - site: "+site+" year: "+year)


def month_data(request, site, year, month):
    return HttpResponse("month_data - site: "+site+" year: "+year+" month: "+month)


def day_data(request, site, year, month, day):
    return HttpResponse("day_data - site: "+site+" year: "+year+" month: "+month+" day: "+day)


def hour_data(request, site, year, month, day, hour):
    return HttpResponse("hour_data - site: "+site+" year: "+year+" month: "+month+" day: "+day+" hour: "+hour)