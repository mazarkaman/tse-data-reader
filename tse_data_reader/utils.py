def normalize_persian_chars(string: str):
    trantab = str.maketrans(
        {'\u064a': '\u06cc',  # yeh
         '\u0649': '\u06cc',  # yeh
         '\u0643': '\u06a9',  # keh
         '\u0651': None,  # tashdid
         '\u0652': None,  # sukon (gerd)
         '\u064b': None,  # fathatan
         '\u064f': None,  # oh
         '\u064e': None,  # fatha
         '\u0650': None,  # kasra
         '\u0640': None,  # kashida __
         '\u0623': '\u0627',  # Alef hamza to alef
         # half spaces'
         '\u200c': ' ',
         '\u200e': ' ',
         '\u200f': ' ',
         '\xa0': ' ',
         '\r': None})
    return string.translate(trantab)
