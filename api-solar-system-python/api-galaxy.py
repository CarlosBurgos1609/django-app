import requests #let 'u get data from api-url'
import os #let 'u execute comands'

def get_data():
    os.system("clear") #Clear screen
    print(":::Solar System Information:::")
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    
    try:
        #requests to API
        response = requests.get(api_url)
        response.raise_for_status() #Read error
        
        data = response.json()
        
        print("### Main menu####")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroid")
        print("[5]. Comets")
        print("[6]. Exit")
        opt = input("::: Press any options:::")
        
    
    
    
    except requests.exceptions.RequestException as e:
        print(f"API error {e}") #=> print("API error",e)
    
        
#Main
info = get_data()
print(info)