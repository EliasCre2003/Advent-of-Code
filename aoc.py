from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


load_dotenv()
cookies = os.getenv('SESSION_COOKIE')
session = requests.Session()
session.cookies.set('session', cookies)

@dataclass
class User:
    user_id: str
    stars: dict[int, dict[int, int]]


def load_user() -> User:
    
    soup = BeautifulSoup(
        session.get("https://adventofcode.com/settings").text, 
        "html.parser"
    )
    user_id = int(soup.article.form.div.label.span.string.removeprefix("(anonymous user #").removesuffix(")"))
    print(user_id)
    
    soup = BeautifulSoup(
        session.get("https://adventofcode.com/events").text,
        "html.parser"
    )
    year_elements = soup.main.article.find_all('div')
    all_progress = {}
    for year_element in year_elements:
        year = int(year_element.a.string.removeprefix("[").removesuffix("]"))
        print(year)
        stars_element = year_element.find("span", {"class": "star-count"})
        if stars_element is None:
            all_progress[year] = 0
            continue
        
        soup = BeautifulSoup(
            session.get(f"https://adventofcode.com/{year}").text,
            "html.parser"
        )
        
        day_elements = soup.main.pre.find_all("a")
        year_progress = {}
        for day_element in day_elements:
            day = int(day_element.find("span", {"class": "calendar-day"}).string)
            print(day)
            star_data = day_element["aria-label"].removeprefix(f"Day {day}, ")
            if star_data == "two stars":
                year_progress[day] = 2
            elif star_data == "one star":
                year_progress[day] = 1
            else:
                year_progress[day] = 0
            print(year_progress[day])
        all_progress[year] = year_progress

    return User(user_id, all_progress)
    


def post_answer(year: int, day: int, answer: str, part: int):
    if 1 > part or 2 < part: raise ValueError(f'Can not post answer to part {part}.')
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.post(
        url + "/answer", 
        data = {'level': part, 'answer': answer},
        cookies = {'session': cookies}
    )
    if response.status_code != 200: 
        raise RuntimeError(f'Something went wrong when submitting answer, status code: {response.status_code}')
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.select_one('main').text)

# post_answer(2025, 1, 6634, 1)

load_user()