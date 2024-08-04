from dataclasses import dataclass


@dataclass
class Article:
    title: str
    summary: str
    image_url: str

@dataclass
class NYTimesArticle:
    title: str
    summary: str
    image_url: str