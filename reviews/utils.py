import re

BAD_WORDS = [
    "sex",
    "porn",
    "ass",
    "penis",
    "pussy",
    "dick",
    "cum",
    "slut",
    "fuck",
    "bitch",
    "nigger",
    "faggot",
    "rape",
    "whore",
    "cunt",
    "nigga",
    "b!tch",
    "f*ck",
    "s3x",
    "p0rn",
    "a$$",
    "p3nis",
    "pussy",
    "d1ck",
    "c*m",
    "sl$t",
    "n@gger",
    "f@got",
    "r@pe",
    "wh0re",
    "c*nt",
    "n1gga",
    "wh@re",
    "b*tch",
    "f#ck",
]

def contains_blocked_words(text):
    if not text:
        return False

    text_lower = text.lower()

    for word in BAD_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        if re.search(pattern, text_lower):
            return True

    return False