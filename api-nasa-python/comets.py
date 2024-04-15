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
        os.system('clear')
        #Absolute magnide
        print(f"Comet name: {data['name']} ")
        #Estimated diameter max(KM)
        print(f"Comet Estimated diameter max(KM): {data['estimated_diameter']['kilometers']['estimated_diameter_max']} ")
        #Estimated diameter min(KM)
        print(f"Comet Estimated diameter min(KM): {data['estimated_diameter']['kilometers']['estimated_diameter_min']} ")
        #Estimated diameter max(FT)
        print(f"Comet Estimated diameter max(FT): {data['estimated_diameter']['feet']['estimated_diameter_max']} ")
        #Estimated diameter min(FT)
        print(f"Comet Estimated diameter min(FT): {data['estimated_diameter']['feet']['estimated_diameter_min']} ")
        #orbutal_data:
            #last_observation_date
        print(f"last_observation_date: {data['orbital_data']['last_observation_date']} ")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
#Main
api_key_nasa = 'mf1ScTVbuUa6Esidx7dxKpsZmnnxxF1Br2Lzb7oi'
get_commet_data(api_key_nasa) 