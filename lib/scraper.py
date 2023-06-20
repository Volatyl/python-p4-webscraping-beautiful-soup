# from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://moringaschool.com/courses/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

courses = doc.select('.leading-relaxed')

for course in courses:
    print(course.contents[0])
