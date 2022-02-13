from bs4 import BeautifulSoup
from requests import get
from random import choice


class QuoteGame:
    def __init__(self):
        self.BASE_URL = "http://quotes.toscrape.com"
        self.url = self.BASE_URL
        self.count = 0
        self.game_over = False
        self.guesses = 4
        self.guess = ""
        self.keep_playing = True
        self.info = self.get_info()
        self.selection = []
        self.hints = []

    def get_soup(self, url):
        response = get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def get_info(self):
        all_quotes = []
        all_authors = []
        all_about_urls = []
        while True:
            soup = self.get_soup(self.url)
            quotes = [text.getText() for text in soup.findAll(class_="text")]
            authors = [text.getText() for text in soup.findAll(class_="author")]
            about_urls = [self.BASE_URL + text.get("href") for text in
                          [tag.find_next_sibling() for tag in soup.findAll(class_="author")]]
            all_authors = all_authors + authors
            all_quotes = all_quotes + quotes
            all_about_urls = all_about_urls + about_urls
            if soup.find(class_="next"):
                self.url = self.BASE_URL + soup.find(class_="next").find_next("a").get("href")
            else:
                info = list(zip(all_quotes, all_authors, about_urls))
                return info

    def init_game(self):
        self.game_over = False
        self.count = 0
        self.guesses = 4
        self.selection = choice(self.info)
        soup = self.get_soup(self.selection[2])
        birthdate = soup.find(class_="author-born-date").getText()
        location = soup.find(class_="author-born-location").getText()
        self.hints = [
                f"The author was born on {birthdate} {location}.",
                f"The author's first name starts with {self.selection[1][0]}.",
                f"The author's last name starts with {self.selection[1].split()[1][0]}"
                ]

    def game_play(self):
        self.init_game()
        print("Here's a quote:\n")
        print(self.selection[0] + "\n")
        while self.guess != self.selection[0]:
            self.guess = input(f"Who said this? Guesses remaining: {self.guesses}. ")
            if self.guess.title() == self.selection[1]:
                print("You guessed correctly! Congratulations!")
                while True:
                    self.keep_playing = input("would you like to play again? (y/n) ")
                    if self.keep_playing == "y":
                        break
                    elif self.keep_playing == "n":
                        self.game_over = True
                        break
                break
            else:
                self.guesses -= 1
                if self.guesses == 0:
                    print("Game Over")
                    while True:
                        self.keep_playing = input("Would you like to play again? (y/n) ")
                        if self.keep_playing == "y":
                            break
                        elif self.keep_playing == "n":
                            self.game_over = True
                            break
                        break
                    if not self.game_over:
                        break
                    break
                else:
                    print(f"Here's a hint: {self.hints[self.count]}")
                    self.count += 1
                    continue
                continue
        return self.game_over


game = QuoteGame()
while True:
    if game.game_play():
        break
