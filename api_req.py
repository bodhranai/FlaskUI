import requests

def call_api():
    # URL of the API endpoint
    api_url = 'http://localhost:5071/api/Proposal/GetProposals'

    try:
        # Sending a GET request to the API
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
        # If an exception occurs during the request, print an error message
        print('Error:', e)
        return None

# Call the function to fetch data from the API
# api_data = call_api()

# # Check if data was fetched successfully
# if api_data is not None:
#     print('Data fetched successfully:', api_data)
# else:
#     print('Failed to fetch data from the API.')
