import json
from pprint import pprint


def count_10_word_in_json():
    from collections import Counter
    with open("newsafr.json", encoding="utf-8") as datafile:
        json_data = json.load(datafile)
        json_items = json_data["rss"]["channel"]["items"]

        descriptions = []

        for i in json_items:
            descriptions.append(i["description"].split())

        format_description = []

        for elem in sum(descriptions, []):
            if len(elem) > 6:
                format_description.append(elem.lower())

        def sortByLength(inputStr):
            return len(inputStr)

        format_description.sort(key=sortByLength, reverse=True)

        Counter = Counter(format_description)
        words = Counter.most_common(10)
        for word in words:
            pprint(f"Слово: '{word[0]}' встречается: {word[1]} раз")


count_10_word_in_json()
