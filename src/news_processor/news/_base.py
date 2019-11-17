# Code by ByungWook.Kang @lesimor
import requests
from bs4 import BeautifulSoup
from news_processor.textrank import KeysentenceSummarizer
from konlpy.tag import Komoran
from typing import List

komoran = Komoran()


def komoran_tokenizer(sent):
    words = komoran.pos(sent, join=True)
    words = [w for w in words if ('/NN' in w or '/XR' in w or '/VA' in w or '/VV' in w)]
    return words


class News:
    TITLE_SELECTOR = ''
    CONTENT_SELECTOR = ''

    def __init__(self, soup: BeautifulSoup):
        self._soup: BeautifulSoup = soup
        self._title: str = self.process_title(soup)
        self._content: str = self.get_content(soup)
        self._sentences: List[str] = self.process_sentences(self._content)

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def sentences(self):
        return self._sentences

    def process_title(self, soup: BeautifulSoup) -> str:
        candidates = soup.select(
            self.TITLE_SELECTOR
        )
        return candidates[0].text

    def get_content(self, soup: BeautifulSoup) -> str:
        # soup 객체로부터 content를 가져옴
        content_from_soup: str = self.process_content(soup)

        # content 후처리.
        content: str = self.postprocess_content(content_from_soup)

        return content

    def process_content(self, soup: BeautifulSoup) -> str:
        candidates = soup.select(
            self.CONTENT_SELECTOR
        )
        return candidates[0].text

    def postprocess_content(self, content: str):
        return content

    def process_sentences(self, content: str) -> List[str]:
        return content.split('.')

    def key_sentences(self, limit=3):
        summarizer = KeysentenceSummarizer(tokenize=komoran_tokenizer, min_sim=0.5)
        selected = summarizer.summarize(self.sentences, topk=limit)
        return [s[2] for s in selected]

    @classmethod
    def get_soup(cls, url) -> BeautifulSoup:
        req = requests.get(url)

        # HTML 소스 가져오기
        html = req.text

        # 내장 html.parser를 이용
        return BeautifulSoup(html, 'html.parser')
