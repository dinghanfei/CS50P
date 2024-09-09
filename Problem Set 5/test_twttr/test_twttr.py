from twttr import shorten

def test_shorten():
    assert shorten("your") == "yr"
    assert shorten("twitter") == "twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("APPLE") == "PPL"
    assert shorten("NAME") == "NM"
