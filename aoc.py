from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup


load_dotenv()
cookies = os.getenv('SESSION_COOKIE')
# url = os.getenv('PUZZLE_URL')
url = 'https://adventofcode.com/2025/day/1/answer'

# with open('input.txt', 'r') as f:
#     personal_input = f.read().rstrip()


# with open('test.txt', 'r') as f:
#     test_input = f.read().rstrip()


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

post_answer(2025, 1, 6634, 1)