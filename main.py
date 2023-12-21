import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
        requrl = requests.get(f"https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(requrl.text, "html.parser")

        title = soup.find(id="firstHeading").text

        print(f"The article is titled: {title}")
        answer = input(f"Would you like to view this article? (Y/N)")

        if answer == "Y":
                webbrowser.open(requrl.url)
                print(f"The url is: {requrl.url}")

                continueprogramme = input("Would you like to read another one? (Y/N)\n").upper()
                if continueprogramme == "Y":
                        pass
                else:
                        break
        elif answer == "N":
                print("Try again!!")
        else:
                print("Please respond with Y or N only.")
