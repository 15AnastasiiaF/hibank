from django.shortcuts import render
import requests
import xmltodict

def index(request):
    return render(request, "index.html")

resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')

resp_parsed = xmltodict.parse(resp.text)
valutes = resp_parsed['ValCurs']['Valute']
for valute in valutes:
    print(valute['Value'], 'рублей за', valute['Nominal'], valute['CharCode'], valute['Name'])
