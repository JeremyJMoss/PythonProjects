from bs4 import BeautifulSoup
from requests import get
from random import choice
keys = ["Quotes", "Authors", "Birth Date", "Birth Location"]
all_quotes = []
all_authors = []
BASE_URL = "http://quotes.toscrape.com"
url = BASE_URL
while True:
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [text.getText() for text in soup.findAll(class_="text")]
    authors = [text.getText() for text in soup.findAll(class_="author")]
    about_urls = [BASE_URL + text.get("href") for text in [tag.find_next_sibling() for tag in soup.findAll(class_="author")]]
    all_authors = all_authors + authors
    all_quotes = all_quotes + quotes
    if soup.find(class_="next"):
        url = BASE_URL + soup.find(class_="next").find_next("a").get("href")
    else:
        info = list(zip(all_quotes, all_authors, about_urls))
        game_over = False
        while not game_over:
            guesses = 4
            selection = choice(info)
            res = get(selection[2])
            more_soup = BeautifulSoup(res.text, "html.parser")
            birthdate = more_soup.find(class_="author-born-date").getText()
            location = more_soup.find(class_="author-born-location").getText()
            print("Here's a quote:\n")
            print(selection[0] + "\n")
            hint = [f"The author was born on {birthdate} {location}.",
                    f"The author's first name starts with {selection[1][0]}.",
                    f"The author's last name starts with {selection[1].split()[1][0]}"
                    ]
            guess = ""
            count = 0
            while guess != selection[1]:
                guess = input(f"Who said this? Guesses remaining: {guesses}. ")
                if guess.title() == selection[1]:
                    print("You guessed correctly! Congratulations!")
                    while True:
                        keep_playing = input("Would you like to play again (y/n)")
                        if keep_playing == "y":
                            break
                        elif keep_playing == "n":
                            game_over = True
                            break
                    break
                else:
                    guesses -= 1
                    if guesses == 0:
                        print("Game Over")
                        while True:
                            keep_playing = input("Would you like to play again (y/n)")
                            if keep_playing == "y":
                                break

                            elif keep_playing == "n":
                                game_over = True
                                break
                            break
                        if not game_over:
                            break
                        continue
                    else:
                        print(f"Here's a hint: {hint[count]}")
                        count += 1
                        continue
                continue
        break


