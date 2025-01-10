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

def extract_title(markdown):
    h1_pattern = r"^# {1}.*"
    title = re.search(h1_pattern, markdown)
    if not title:
        raise Exception("Missing h1 tag")
    res = title.group(0)
    res = res[2:]
    return res.strip()
