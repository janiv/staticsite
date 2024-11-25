import re

def extract_markdown_images(text):
    alt_matches = re.findall(r"(?<=!\[).*?(?=\])", text)
    url_matches = re.findall(r"(?<=\().*?(?=\))", text)
    tuples = tuple(zip(alt_matches, url_matches))
    return list(tuples)


def extract_markdown_links(text):
    link_matches = re.findall(r"(?<=\[).*?(?=\])", text)
    url_matches = re.findall(r"(?<=\().*?(?=\))", text)
    tuples = tuple(zip(link_matches, url_matches))
    return list(tuples)



text = "This is a text with ![something] but no url"
print(extract_markdown_images(text))
