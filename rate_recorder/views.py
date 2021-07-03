import json
from datetime import date

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict

from rate_recorder.models import Rates


def dashboard_view(request):
    today = date.today()
    current_date = today.strftime('%Y-%m-%d')
    current_rates = Rates.objects.filter(date_created=current_date)
    filtered_rates = current_rates[len(current_rates) - 3:]
    return render(request, 'index.html', {'current_rates': filtered_rates})


def search_rates_by_date(request):
    requested_date = json.loads(request.body)['search_date']
    filtered_rates = requested_rates = Rates.objects.filter(date_created=requested_date)
    if requested_rates:
        filtered_rates = requested_rates[len(requested_rates) - 3:]

    formatted_rates = {}
    for rate in filtered_rates:
        formatted_rates[rate.bank.name] = model_to_dict(rate)
        formatted_rates[rate.bank.name]['date_created'] = rate.date_created.strftime('%Y-%m-%d')

    # filtered_rates = serializers.serialize('json', filtered_rates)
    # return HttpResponse(formatted_rates, content_type="application/json")
    return JsonResponse(formatted_rates, safe=False)
    # return render(request, 'index.html', {'rates_by_date': filtered_rates})
