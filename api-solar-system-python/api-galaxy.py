import requests #let 'u get data from api-url'
# pip install requests
import os #let 'u execute comands'

#1. Crear un menu
def diplay():
    print("---------------------------------")
    print("---------------------------------")
    print("### MAIN MENU####")
    print("[1]. Planets")
    print("[2]. Moons")
    print("[3]. Stars")
    print("[4]. Asteroid")
    print("[5]. Comets")
    print("[6]. Exit")
    opt = input("::: Press any options:::")
    print("---------------------------------")
    print("---------------------------------")
    return opt
#2.  De la opción seleccionada, visualizar los siguientes campos: "English name","Gravity",  "inclination", "Is planet?"
def evaluate(option, info):
    if (option == '1'):
        planets = list(filter(lambda x: x['bodyType'] == "Planet", info['bodies']))
        
        for planet in planets:
            print("English name: "  + planet['englishName'] + "  Gravity: " + str(planet['gravity']) + "  Inclination: " + str(planet['inclination']) + "  Is planet?: " + str(planet['isPlanet']))
    if (option == '2'):
        moons = list(filter(lambda x: x['bodyType'] == "Moon", info['bodies']))
        
        for moon in moons:
            print("English name: "  + moon['englishName'] + "  Gravity: " + str(moon['gravity']) + "  Inclination: " + str(moon['inclination']) + "  Is planet?: " + str(moon['isPlanet']))
    if (option == '3'):
        stars = list(filter(lambda x: x['bodyType'] == "Star", info['bodies']))
        
        for star in stars:
            print("English name: "  + star['englishName'] + "  Gravity: " + str(star['gravity']) + "  Inclination: " + str(star['inclination']) + "  Is planet?: " + str(star['isPlanet']))
    if (option == '4'):
        asteroids = list(filter(lambda x: x['bodyType'] == "Asteroid", info['bodies']))
        
        for asteroid in asteroids:
            print("English name: "  + asteroid['englishName'] + "  Gravity: " + str(asteroid['gravity']) + "  Inclination: " + str(asteroid['inclination']) + "  Is planet?: " + str(asteroid['isPlanet']))
    if (option == '5'):
        comets = list(filter(lambda x: x['bodyType'] == "Comet", info['bodies']))
        
        for comet in comets:
            print("English name: "  + comet['englishName'] + "  Gravity: " + str(comet['gravity']) + "  Inclination: " + str(comet['inclination']) + "  Is planet?: " + str(comet['isPlanet']))

def get_data():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error {e}")

os.system("clear")
print(":::Solar System Information:::")
info = get_data()
option = diplay()

while option != '6':
    evaluate(option, info)
    option = diplay()