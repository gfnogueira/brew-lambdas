import json
import urllib.request

def lambda_handler(event, context):
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    dolar = data['USDBRL']['bid']
    print(f"Current dollar rate: R${dolar}")
    return {
        'statusCode': 200,
        'body': json.dumps({'dolar': dolar})
    }
