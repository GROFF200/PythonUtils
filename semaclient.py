import requests
import time

# Replace with your actual username and password
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
BASE_URL = 'https://sdc.semadatacoop.org/sdcapi'

def get_token(username, password):
    url = f'{BASE_URL}/token/get'
    params = {
        'userName': username,
        'password': password
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['success']:
        return data['token']
    else:
        raise Exception(f"Failed to get token: {data['message']}")

def get_brand_datasets(token):
    url = f'{BASE_URL}/export/branddatasets'
    params = {
        'token': token
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    try:
        # Step 1: Get the security token
        token = get_token(USERNAME, PASSWORD)
        print(f"Token: {token}")
        
        # Step 2: Fetch brand datasets
        brand_datasets = get_brand_datasets(token)
        if brand_datasets['success']:
            print("Brand Datasets:")
            for dataset in brand_datasets['BrandDatasets']:
                print(f"- {dataset['BrandName']} (ID: {dataset['DatasetId']})")
        else:
            print(f"Failed to fetch brand datasets: {brand_datasets['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
