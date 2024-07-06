import requests



""" this function is used to get data from the API and print bitcoin price """
def get_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON data from the response
        print(data['bpi']['USD']['rate'])
    else:
        print(f"Failed to retrieve data: {response.status_code}")