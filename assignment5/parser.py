def parse_nwodkram(text):
    import re
    old_text = text
    # Replacing <imgURL>(w=nr1,h=nr2) with <img src="imgURL" width="nr1" heigth="nr2"
    # We do this one first, so it doesn't interfere with <b> and <i> later on.
    text = re.sub(r'\<(.+?)\>\(w=(\d+?),h=(\d+?)\)', r'<img src="\1" width="\2" heigth="\3">', text)

    # text = re.sub(r'%(.+?)%', r'<b>\1</b>', text)   # Replacing %text% with <b>text<\b>
    # text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)   # Replacing *text* with <i>text<\i>
    text = re.sub(r'(?<!\\)\%(.+?)(?<!\\)\%', r'<b>\1</b>', text)   # Replacing %text% with <b>text<\b>
    text = re.sub(r'(?<!\\)\*(.+?)(?<!\\)\*', r'<i>\1</i>', text)   # Replacing *text* with <i>text<\i>

    text = re.sub(r'\\\*', r'*', text)
    text = re.sub(r'\\\%', r'*', text)

    # Replacing [link](text) with <a href="link">text<\a>
    # Current solution is to first remove any https:// or http:// from links, and then add them.
    text = re.sub(r'\[(.+?)\]\((?:https://|http://)(.+?)\)', r'[\1](\2)', text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"<a href='https://\2'>\1</a>", text)

    # Substituting >> TEXT with <blockquote>TEXT</blockquote>.
    # TODO: Make sure it works when blockquote isnt on first line
    text = re.sub(r'^>>(.+)', r'<blockquote>\1</blockquote>', text)

    # Replacing [wp:some_keyword] with a Wikipedia-link to the "some_keyword" article.
    text = re.sub(r'\[wp:(.+?)\]', r'<a href="https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1">\1</a>', text)

    # print(old_text, "\n" + text)
    return text
parse_nwodkram(text)
