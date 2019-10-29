import requests
import re


def get_content():
    content = requests.get("http://book.douban.com");
    html = content.text
    return html


def get_book_title():
    # regex = '<div class="title".*?class="" href="(.*?)".*?>(.*?)</a>'
    regex = '<div class="info".*?class="title".*?class="" href="(.*?)".*?>(.*?)</a>.*?class="author">(.*?)</div>'
    results = re.findall(regex, get_content(), re.S)
    print(results)
    return len(results)


def get_book_user():
    regex = '<div class="info".*?class="author">(.*?)</div>'
    results = re.findall(regex, get_content(), re.S)
    print(results)
    return len(results)


if __name__ == '__main__':
    print(get_book_title())
