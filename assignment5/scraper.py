import re

def find_emails(text):
    name = r'[\w\.#%&~,\*\\?_\{\}]+?'
    server = r'[\w\.#%&~,\*\\?_\{\}]+?'
    domain = r'[a-zA-Z][a-zA-Z\.]*[a-zA-Z]'  # NOTE: not including one-character domains

    email_regex = name + r'@' + server + r'\.' + domain

    emails = re.findall(email_regex, text)

    return emails


def find_urls(text):
    protocol = r'https?'  # http with optional s
    host = r'[\w\.\-~]+?'
    path = r'[\w\.\-~\/]+?' # Implementing domain and path seperately makes no sense, as they combined can contain arbritrary numbers of .s and /s, and we have no need to capture them seperately. There is also no reason to single out the www, as it is a legal part of the path-regex.

    url_regex = r"""\<a href=["|'](""" + protocol + """://""" + host + """\.""" + path + """)["|']\>.*?\</a\>"""  #TODO: Figure out how to make the strings match.

    url_matches = re.findall(url_regex, text)
    return url_matches



import requests
def all_the_emails(url, depth):
    if depth <= 2:
        print("######## Entering depth %d, adress %s ########" % (depth, url))
        depth += 1
        response = requests.get(url)
        page = str(response.content)
        emails = find_emails(page)
        url = find_urls(page)
        print(emails)
        print(url)
        print(page)


if __name__ == "__main__":
