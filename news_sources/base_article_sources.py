from typing import Dict, List
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent

from news_sources.types import Article


class BaseArticleSource(ABC):
    def __init__(self, url):
        self.pared_source = BeautifulSoup(
            self._make_request(url=url, headers=self._get_headers()),
            features="lxml"
        )

    def get_news(self) -> List[Article]:
        raw_articles = self._get_raw_today_news()
        return self._map_raw_news(raw_news=raw_articles)

    @staticmethod
    def _get_headers():
        ua = FakeUserAgent()
        return {
            "User-Agent": ua.random
        }
    @staticmethod
    def _make_request(url,headers, method="GET"):
        return requests.request(method=method, url=url, headers=headers).content

    @abstractmethod
    def _get_raw_today_news(self) -> List[BeautifulSoup]:
        pass

    @abstractmethod
    def _map_raw_news(self, raw_news: List[BeautifulSoup]) -> List[Article]:
        pass

    @abstractmethod
    def _get_article_url(self, raw_articles: BeautifulSoup) -> str:
        pass


    def _get_article_soup(self, raw_articles) -> BeautifulSoup:
        article_url = self._get_article_url(raw_articles=raw_articles)
        return BeautifulSoup(
            self._make_request(
                url=article_url,
                headers=self._get_headers()
            ),
            features="lxml"
        )

    @abstractmethod
    def _get_title(self, article_soup:BeautifulSoup) -> str:
        pass

    @abstractmethod
    def _get_summary(self, article_soup:BeautifulSoup) -> str:
        pass

    @abstractmethod
    def _get_image_url(self,article_soup:BeautifulSoup) -> str:
        pass

