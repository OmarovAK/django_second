from django.core.paginator import Paginator
from django.shortcuts import render
import os
import csv


def list_station(request):
    num_page = request.GET.get('page_', 1)

    file = os.path.join(os.getcwd(), 'data-398-2018-08-30.csv')
    list_station__ = list()
    with open(file, encoding='utf-8', mode='r') as list_station_:
        csv_reader = csv.DictReader(list_station_)
        for i in csv_reader:
            list_station__.append(i)
    for i in list_station__:
        print(i)

    paginator = Paginator(list_station__, 10)

    page = paginator.get_page(num_page)

    my_dict = {
        'title': 'Список станций',
        'page': page,
        'num_page': num_page
    }
    return render(request, 'pagination/index.html', my_dict)
