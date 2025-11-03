
import pytest

#
# straightforward test
#
def test_simple():
    assert count_words("hello") == 1


#
# test for error
#
def _test_error():
    with pytest.raises(ValueError):
        count_words(777)


#
# test with a fixtre
#
@pytest.fixture
def zen_text():
    """reads a sample text from a file"""
    print("preparing test")
    with open("zen_of_python.txt") as f:
        yield f.read()
    print("cleaning up")

def _test_long(zen_text):  # TODO: remove underscore
    assert count_words(zen_text) > 100


#
# test with parametrization
#
EXAMPLES = [
    ("", 0),
    ("hello", 1),
    ("hello world", 2),
    ("the quick brown fox jumps over the lazy dog", 9),
    ("are-words-with-hyphens-one-or-many?", 7),
    ("säuerliche Brühe", 2),
    ("123 456 789", 0),
]
@pytest.mark.parametrize("text,nwords", EXAMPLES)
def _test_examples(text, nwords):  # TODO: remove underscore
    assert count_words(text) == nwords
