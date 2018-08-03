# coding=UTF-8
import requests
from bs4 import BeautifulSoup


class ExtractWord:

    def __init__(self):
        pass

    def extract_word(css_url, word_code):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                          '537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        css_str = requests.get(css_url, headers=headers).text.strip()
        x_start = int(css_str.index(word_code) + 20)
        x_end = css_str.index(".", x_start)
        x = int(css_str[x_start:x_end])
        y_end = css_str.index(".0px;}", x_start)
        y_start = int(x_end + 6)
        y = int(css_str[y_start:y_end])
        svg_path_start = int(css_str.index("url") + 4)
        svg_path_end = css_str.index(")", svg_path_start)
        svg_path = css_str[svg_path_start:svg_path_end]
        svg_path = svg_path.replace("address.", "review.")
        resp = requests.get('http:' + svg_path, headers=headers)
        soup = BeautifulSoup(resp.content, features='lxml')
        [s.extract() for s in soup('style')]
        index = int(x / 14 + int(y / 30) * 43)
        return soup.text.strip()[index]
