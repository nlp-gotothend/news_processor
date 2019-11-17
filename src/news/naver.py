# Code by ByungWook.Kang @lesimor
from src.news import News


class NaverNews(News):
    TITLE_SELECTOR = '#articleTitle'
    CONTENT_SELECTOR = '#articleBodyContents'

    def postprocess_content(self, content: str):
        sentences = content.strip().split('.')[1:]
        sentences = [s.strip() for s in sentences]
        return '. '.join(sentences)


if __name__ == '__main__':
    # GET 요청으로 페이지 내용을 가져온다.
    url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=025&aid=0002953341&date=20191117&type=1&rankingSeq=1&rankingSectionId=100'
    news = NaverNews(News.get_soup(url))

    print(news.title)
    print(news.content)
