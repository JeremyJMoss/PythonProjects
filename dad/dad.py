import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import cprint

cprint(figlet_format("DAD JOKE 3000"), "magenta")
topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url, headers={"Accept": "application/json"}, params={"term": topic})
data = res.json()["results"]
try:
    joke_dict = choice(data)
except IndexError:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
else:
    print(f"I've got {len(data)} about {topic}. Here's one: ")
    print(f" {joke_dict['joke']}")
