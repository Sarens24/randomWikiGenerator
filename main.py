import requests
from bs4 import BeautifulSoup
import webbrowser
from termcolor import colored

while True:
    content = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Special:Random").content, "html.parser")
    title = content.find(class_="firstHeading").text

    print(colored(f"{title}", 'green'))
    print(colored("Do you want to view it? (Y/N/Q)", 'cyan'))

    answer = input("").lower()

    if answer == "y":
        print(colored("Enjoy!", 'magenta'))
        webbrowser.open("https://en.wikipedia.org/wiki/%s" % title)
        break
    elif answer == "n":
        print(colored("How about this one?", 'yellow'))
        continue
    elif answer == 'q':
        print(colored("See ya later!", 'magenta'))
        break
    else:
        print(colored("Response must be Y/N!", 'red'))
        continue
