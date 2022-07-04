from bbquote913.lib import get_quote

def testing_get_quote():
    
    response = get_quote()
    assert len(response) != 0
