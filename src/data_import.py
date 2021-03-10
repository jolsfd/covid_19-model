import requests
import time
import os

# Global variables
URL = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
Path = 'data/covid_data.csv'

def url_request(url):
    start = time.time()

    response = requests.get(url)

    end = time.time()
    response_time = str(end - start)
    
    if response.status_code == 200:
        # Encoding without BOM
        response.encoding = 'utf-8-sig'

        return response.text, response_time

    else:
        print('Error in API Request')

def save_response(text, path_to_file):
    file = open(path_to_file, 'w' , encoding='utf-8')

    file.write(text)

    file.close()

def update(Path=Path,URL=URL):
    # Send request to url
    response_text, response_time = url_request(URL)

    # Save data
    save_response(response_text, Path)

    # Response time Output
    print('{}s for response'.format(response_time))