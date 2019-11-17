# Code by ByungWook.Kang @lesimor
from src.news_processor.news import News
import re


class NaverNews(News):
    TITLE_SELECTOR = '#articleTitle'
    CONTENT_SELECTOR = '#articleBodyContents'

    def postprocess_content(self, content: str):
        sentences = content.strip().split('.')[1:]
        sentences = [s.strip() for s in sentences]

        # 뒤어서부터 탐색하면서 이메일 형식이 있는 문장의 index를 찾는다.
        limit_index = -1
        for idx, sent in reversed(list(enumerate(sentences))):
            if re.match(r'.*@.*', sent):
                limit_index = idx
                break
        if limit_index != -1:
            sentences = sentences[:limit_index]
        return '. '.join(sentences)

    def process_sentences(self, content: str):
        sentences = content.strip().split('.')[1:]

        # TODO: 기사가 너무 짧으면 핵심문장 추출 단계에서 에러 발생.
        # None 또는 '' 제거.
        # sentences = [s for s in sentences if bool(s)]

        return [s.strip() for s in sentences]


if __name__ == '__main__':
    # GET 요청으로 페이지 내용을 가져온다.

    urls = [
        'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=025&aid=0002953363',
        'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=449&aid=0000181391',
        'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=022&aid=0003414844'
    ]

    for url in urls:
        news = NaverNews(News.get_soup(url))
        print('--------------------')
        print(news.title)
        print(news.content)
        print(news.key_sentences())
