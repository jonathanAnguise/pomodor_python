import sys
import time
from os import system


class DisplayManager:

    def __init__(self):
        self.tomato = "🍅"
        self.coffee = "☕"
        self.eating_emoji = "😋"
        self.list_to_display = []
        self.index_of_tomato_to_eat = 0

    def create_initial_string(self, breaking_time=5, run_time=25):
        for turn in range(run_time):
            self.list_to_display.append(self.tomato)
        self.list_to_display.append(self.coffee)

    def eat_tomato_string(self):
        if self.tomato in self.list_to_display:
            self.index_of_tomato_to_eat = self.list_to_display.index(self.tomato)
            self.list_to_display[self.index_of_tomato_to_eat] = self.eating_emoji
        else:
            print("Don't eat more tomato")

    def clean_terminal(self):
        system('clear')


if __name__ == "__main__":
    my_display = DisplayManager()
    my_display.create_initial_string()
    for i in range(29):
        time.sleep(1)
        my_display.clean_terminal()
        print(*my_display.list_to_display)
        my_display.eat_tomato_string()
