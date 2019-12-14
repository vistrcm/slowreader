import random
import time

from requests_html import HTMLSession


def get_wiki_text(session):
    r = session.get('https://en.wikipedia.org/wiki/Special:Random', allow_redirects=True)
    head = r.html.find('#firstHeading', first=True).text
    text = r.html.find("#mw-content-text", first=True).text
    return head + "\n" * 2 + text


def get_delay(mu=0.5, sigma=0.2):
    return max(0, random.normalvariate(mu, sigma))


def delayed_print(txt):
    for symbol in txt:
        print(symbol, end="")
        delay = get_delay()
        time.sleep(delay)


def main():
    session = HTMLSession()

    while True:
        txt = get_wiki_text(session)
        delayed_print(txt)


if __name__ == "__main__":
    main()
