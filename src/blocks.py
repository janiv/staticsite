def markdown_to_blocks(markdown):
    res = []
    temp = markdown.split("\n\n")
    for item in temp:
        if not item:
            continue
        item = item.strip()
        res.append(item)
    return res
