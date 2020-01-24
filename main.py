import random
import time

from requests_html import HTMLSession


def get_wiki_text(session):
    r = session.get('https://en.wikipedia.org/wiki/Special:Random', allow_redirects=True)
    head = r.html.find('#firstHeading', first=True).text
    text = r.html.find("#mw-content-text", first=True).text
    return head + "\n" * 2 + text


def get_rfc_text(session):
    while True:
        try:
            suggestion = random.randint(0, 9000)
            # suggestion = 2616
            r = session.get(f"https://www.rfc-editor.org/rfc/rfc{suggestion}.txt")
            r.raise_for_status()
            break # exit if everything is ok
        except Exception:
            print("cant' find RFC {suggestion}")

    text = r.text
    return text


def get_random_text(session):
    return get_rfc_text(session)


def get_delay(mu=0.3, sigma=0.2):
    """assuming 200 characters per minute delay mu should be ~0.3"""
    return max(0, random.normalvariate(mu, sigma))


def delayed_print(txt):
    for symbol in txt:
        print(symbol, end="", flush=True)
        delay = get_delay()
        time.sleep(delay)


def main():
    session = HTMLSession()

    while True:
        txt = get_random_text(session)
        delayed_print(txt)
        print("\n" * 10)


if __name__ == "__main__":
    main()
