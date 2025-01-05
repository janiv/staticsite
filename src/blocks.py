import re


def markdown_to_blocks(markdown):
    res = []
    temp = markdown.split("\n\n")
    for item in temp:
        if not item:
            continue
        item = item.strip()
        res.append(item)
    return res

def block_to_block_type(block):
    headings_pattern = r"^[#]{1,6}[ ][\S]"
    if(re.search(headings_pattern, block)):
        return "heading"
    if(block[0:3]=="```" and block[:-3]=="```"):
        return "code"
    
    # Check if quote or unordered list
    lines = block.split('\n')
    line_count = len(lines)
    q_count = 0
    uo_list_count = 0
    for line in lines:
        if line[0] == ">":
            q_count += 1
        if line[:2] == "- " or line[:2]== "* ":
            uo_list_count += 1
    if q_count == line_count:
        return "quote"
    if uo_list_count == line_count:
        return "unordered list"
    
    # Check if ordered list
    is_ordered_list = True
    numbered_list_pattern = r"^[\d]*\.[ ]"
    prev = 0
    for i in range(0, line_count):
        num_match = re.search(numbered_list_pattern, lines[i])
        if not num_match:
            is_ordered_list = False
            break
        num_string = num_match.group(0)
        num_string = num_string[:-2]
        num_val = int(num_string)
        if(num_val - prev != 1):
            is_ordered_list = False
            break
        prev = num_val
    if(is_ordered_list):
        return "ordered list"
    return "normal"