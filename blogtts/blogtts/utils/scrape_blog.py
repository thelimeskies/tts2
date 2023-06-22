import json
import re

import requests
from bs4 import BeautifulSoup


class Scrape:
    def __init__(self, url) -> None:
        self.url = url

    def get_json(self):
        r = requests.get(self.url)
        return r

    def number_of_posts(self):
        data = self.get_json()
        parsed = json.loads(data.text)
        return len(parsed["all"])

    def get_post(self, post_number):
        data = self.get_json()
        parsed = json.loads(data.text)
        return parsed["all"][post_number]

    def get_post_title(self, post_number):
        post = self.get_post(post_number)
        return post["title"]

    def get_post_body(self, post_number):
        post = self.get_post(post_number)
        cleaned_text = re.sub(r"__(.*?)__", r"\1", post["body"])
        return cleaned_text

    def get_post_author(self, post_number):
        post = self.get_post(post_number)
        return post["first_name"] + " " + post["last_name"]

    def get_post_date(self, post_number):
        post = self.get_post(post_number)
        return post["published_at"]

    def clean_body(self, post_number):
        # get post body
        body = self.get_post_body(post_number)

        pattern = r"Introduction([\s\S]*)REFERENCES"

        # Extract the main content using regex
        main_content = re.search(pattern, body)

        if not main_content:
            pattern = r"Introduction([\s\S]*)References"
            main_content = re.search(pattern, body)

        try:
            article = main_content.group(1)
        except AttributeError:
            article = None

        if not article:
            article = body
        # Remove citations
        # Remove citations in the format "Author et al., Year" or "Author et al. (Year)"
        cleaned_text = re.sub(
            r"\((?:[\w\s]+,?\s?)+\)|[\w\s]+ et al.,? \(\d+\)", "", article
        )
        cleaned_text = re.sub(r"\(\w+(?: et al\., \d+)?\)", "", cleaned_text)

        # Remove extra spaces and line breaks
        cleaned_text = re.sub(r"\s+", " ", cleaned_text)

        return cleaned_text

    def clean_title(self, post_number):
        # get post title
        title = self.get_post_title(post_number)
        # remove html tags
        soup = BeautifulSoup(title, "html.parser")
        title = soup.get_text()
        # remove newlines
        title = title.replace("\n", " ")

        return title

    def clean_author(self, post_number):
        # get post author
        author = self.get_post_author(post_number)
        # remove html tags
        soup = BeautifulSoup(author, "html.parser")
        author = soup.get_text()
        # remove newlines
        author = author.replace("\n", " ")

        return author

    def get_url(self, post_number):
        base_url = "https://fedgen.net/phis/read/"
        post = self.get_post(post_number)
        return base_url + post["slug"]


if __name__ == "__main__":
    scrape = Scrape("https://fedgen.ml/content/latest")
    print(scrape.number_of_posts())
    # print(scrape.get_post(0))
    # print(scrape.get_post_title(0))
    # print(scrape.get_post_body(2))
    # print(scrape.clean_body(1))
