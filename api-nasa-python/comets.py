import requests
import os

def get_commet_data(api_key):
    print("::: COMETS INFORMATION")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        #Show:
        #Comet name
        # os.system('clear')
        #Absolute magnide
        print(f"Comet name: {data['name']} ")
        #Estimated diameter max(KM)
        #Estimated diameter min(KM)
        #Estimated diameter max(FT)
        #Estimated diameter min(FT)
        #orbutal_data:
            #last_observation_date
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
#Main
api_key_nasa = 'mf1ScTVbuUa6Esidx7dxKpsZmnnxxF1Br2Lzb7oi'
get_commet_data(api_key_nasa) 