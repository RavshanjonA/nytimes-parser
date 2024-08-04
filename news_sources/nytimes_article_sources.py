from typing import List, Any

from bs4 import BeautifulSoup

from news_sources.base_article_sources import BaseArticleSource
from news_sources.types import NYTimesArticle


class NYTimesNewsSource(BaseArticleSource):
    SOURCE_MAIN_URL = 'https://www.nytimes.com'

    def __init__(self):
        super().__init__(url=f"{self.SOURCE_MAIN_URL}/section/world")

    def _get_raw_today_news(self) -> List[Any]:
        return self.pared_source.find_all(name="div", attrs={'class': "css-1cp3ece"})

    def _map_raw_news(self, raw_news: List[BeautifulSoup]) -> List[NYTimesArticle]:
        result = []
        for raw_one_new in raw_news:
            article_soup = self._get_article_soup(raw_articles=raw_one_new)
            try:
                result.append(
                    NYTimesArticle(
                        title=self._get_title(article_soup),
                        summary=self._get_summary(article_soup),
                        image_url=self._get_image_url(article_soup)
                    )
                )
            except Exception:
                pass
        return result

    def _get_article_url(self, article_soup: BeautifulSoup) -> str:
        endpoint = article_soup.find(name="a").attrs["href"]
        return f"{self.SOURCE_MAIN_URL}/{endpoint}"

    def _get_title(self, article_soup: BeautifulSoup) -> str:
        return article_soup.find("h1").text

    def _get_summary(self, article_soup: BeautifulSoup) -> str:
        return article_soup.find(name="p", attrs={"id": "article-summary"}).text

    def _get_image_url(self, article_soup: BeautifulSoup) -> str:
        return article_soup.find(name="img").attrs['srcset'].split(",")[-1].split(" ")[0]
if __name__ == '__main__':
    source = NYTimesNewsSource()
    print(source.get_news())