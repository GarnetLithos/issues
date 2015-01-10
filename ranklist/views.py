from django.shortcuts import render


def bullets1(request):
    return render(request, 'ranklist/bullets/bullets1.html', )


def bullets2(request):
    return render(request, 'ranklist/bullets/bullets2.html', )


def sort_bar_chart(request):
    return render(request, 'ranklist/sortableBarChart/sortBarChart.html', )


def base(request):
    return render(request, 'ranklist/base.html', )


def hours(request):
    return render(request, 'ranklist/hours.html', )


def days(request):
    return render(request, 'ranklist/days.html', )


def months(request):
    return render(request, 'ranklist/months.html', )


def years(request):
    return render(request, 'ranklist/years.html', )
