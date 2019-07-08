import xml.etree.ElementTree as ET


def count_10_word_in_xml():
    from collections import Counter
    tree = ET.parse("newsafr.xml")
    descriptions = []
    root = tree.getroot()
    xml_items = root.findall("channel/item")

    for item in xml_items:
        description = item.find("description")
        descriptions += description.text.split()

    format_description = []
    for word in descriptions:
        if len(word) > 6:
            format_description.append(word.lower())

    def sortByLength(inputStr):
        return len(inputStr)

    format_description.sort(key=sortByLength, reverse=True)

    Counter = Counter(format_description)
    words = Counter.most_common(10)
    for word in words:
        print(f"Слово: '{word[0]}' встречается: {word[1]} раз")


count_10_word_in_xml()
