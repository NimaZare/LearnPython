from hello import hello


def test_default():
    assert hello() == "Hello, world!"


def test_argument():
    assert hello("Nima") == "Hello, Nima!"

# For run this test
# command:  pytest
# Or
# command:  pytest .\test\test_hello.py