from django.shortcuts import render, redirect
from django.http import JsonResponse
import json, os, requests

# Create your views here.
def index(req):
    return render(req, 'index.html')

def convert(req):
    # send a request to the api from here
    api_key = os.getenv('API_KEY')
    if req.method == 'POST':
        amount = req.POST.get('amount')
        from_currency = req.POST.get('from_currency')
        to_currency = req.POST.get('to_currency')
    # sample url form the api that suppost pair conversion 
    # GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP/AMOUNT
    api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}'

    # get request to the api end point
    response = requests.get(api_url)

    if response.status_code == 200 :
        data = response.json()
        # log the response data first
        return render(req, 'result.html', {'data' : data, 'amount' : amount})
    else :
        return JsonResponse({'error': 'An error occurred while fetching data from the API.'}, status=500)