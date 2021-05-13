# write your code here!
import requests
import json
cache = {}
eur = requests.get('http://www.floatrates.com/daily/eur.json').text
cache['usd'] = 1
cache['eur'] = json.loads(eur)['usd']['rate']
input_currency = input()
if input_currency.upper() != 'USD':
    url = 'http://www.floatrates.com/daily/' + input_currency + '.json'
    r = requests.get(url).text
    rate = json.loads(r)
    cache[input_currency] = rate['usd']['rate']
in_cache = False
while True:
    output_currency = input()
    if not output_currency:
        break
    input_amount = float(input())
    in_cache = True
    print('Checking the cache...')
    if output_currency not in cache:
        url = 'http://www.floatrates.com/daily/' + output_currency + '.json'
        r = requests.get(url).text
        rate = json.loads(r)
        cache[output_currency] = rate['usd']['rate']
        in_cache = False
    output_amount = round(input_amount * cache[input_currency] / cache[output_currency], 2)
    if in_cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
    print('You received {0} {1}.'.format(output_amount, output_currency.upper()))


