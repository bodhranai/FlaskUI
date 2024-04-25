import requests

def call_api(url):
   
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print('Failed to fetch data from API:', response.status_code)
            return None
    except Exception as e:
        print('Error:', e)
        return None


