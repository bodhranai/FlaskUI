import requests

def call_api():
    # URL of the API endpoint
    api_url = 'http://localhost:5071/api/Proposal/GetProposals'

    try:
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            data = response.json()
            return data
        else:
            # If the request was not successful, print an error message
            print('Failed to fetch data from API:', response.status_code)
            return None
    except Exception as e:
        print('Error:', e)
        return None


