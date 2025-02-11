import requests
import re
from collections import Counter


def find_common_words(url_list: list) -> list:
    words_counter = Counter()
    regular_exp = re.compile(r'\b\w+\b')
    for url in url_list:
        response = requests.get(url)
        words = regular_exp.findall(response.text, re.I)
        words_counter.update(Counter(words))

    return words_counter.most_common()

most_common_words = find_common_words(['https://example.com', "https://httpbin.org", "https://random-data-api.com"])

print(most_common_words)