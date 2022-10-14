import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://developer.android.com/reference/android/R.anim")
soup = BeautifulSoup(webpage.content,"html.parser")

print(soup)