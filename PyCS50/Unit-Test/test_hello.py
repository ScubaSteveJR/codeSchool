from hello import hello

def test_default():
    assert hello() == "hello, Stephen"

def test_argument():
    assert hello("Stephen") == "hello, Stephen"
