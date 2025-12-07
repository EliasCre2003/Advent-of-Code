from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup


load_dotenv()
cookies = os.getenv('SESSION_COOKIE')
# url = os.getenv('PUZZLE_URL')
url = 'https://adventofcode.com/2021/day/3/answer'

# with open('input.txt', 'r') as f:
#     personal_input = f.read().rstrip()


# with open('test.txt', 'r') as f:
#     test_input = f.read().rstrip()


def post_answer(answer: str, part: int):
    if 1 > part or 2 < part: raise ValueError(f'Can not post answer to part {part}.')
    response = requests.post(
        url, 
        data={'level': part, 'answer': answer},
        cookies={'session': cookies}
    )
    if response.status_code != 200: 
        raise RuntimeError(f'Something went wrong when submitting answer, status code: {response.status_code}')
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.select_one('main').text)