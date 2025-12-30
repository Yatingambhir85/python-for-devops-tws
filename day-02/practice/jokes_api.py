import requests

pj_url = 'https://official-joke-api.appspot.com/random_joke'
dad_joke_url = "https://icanhazdadjoke.com/"


def get_joke(url_type,mood):
    headers = {'Accept': 'application/json'}
    response = requests.get(url=url_type,headers=headers)
    if mood == 'dad':
        final_joke = response.json()["joke"]
    else:
        final_joke = response.json()["setup"] + " ... " + response.json()["punchline"]
    return final_joke


mood=input("Which joke would you like to hear? (dad/pj): ")
if mood =='dad':
    url_type= dad_joke_url
elif mood =='pj':
    url_type= pj_url
else:
    url_type= dad_joke_url

final_joke=get_joke(url_type,mood)
print(final_joke)