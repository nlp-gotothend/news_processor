# Code by ByungWook.Kang @lesimor
from src.news import News
from src.constants import EMAIL_REGEX
import re


class NaverNews(News):
    TITLE_SELECTOR = '#articleTitle'
    CONTENT_SELECTOR = '#articleBodyContents'

    def postprocess_content(self, content: str):
        sentences = content.strip().split('. ')[1:]
        sentences = [s.strip() for s in sentences]
        return '. '.join(sentences)

    def process_sentences(self, content: str):
        sentences = content.strip().split('. ')[1:]

        # TODO: 기사가 너무 짧으면 핵심문장 추출 단계에서 에러 발생.
        # None 또는 '' 제거.
        # sentences = [s for s in sentences if bool(s)]

        # 뒤어서부터 탐색하면서 이메일 형식이 있는 문장의 index를 찾는다.
        # TODO: 뒤에 불필요한 내용 자르기
        # limit_index = -1
        # for idx, sent in reversed(list(enumerate(sentences))):
        #     print(sent)기
        #     if re.match(EMAIL_REGEX, sent):
        #         print('걸렸다!')
        #         limit_index = idx
        #         break
        # if limit_index != -1:
        #     sentences = sentences[:limit_index]

        return [s.strip() for s in sentences]


if __name__ == '__main__':
    # GET 요청으로 페이지 내용을 가져온다.
    url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=025&aid=0002953363'
    news = NaverNews(News.get_soup(url))

    print(news.title)
    print(news.content)
    print(news.key_sentences())
