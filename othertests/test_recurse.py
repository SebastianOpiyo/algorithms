# test case for recursion
from recurse import recurse
from io import StringIO
import sys


def test_recurse_output():
    """Test that the recursion function produces the expectedoutput."""
    captured_output = StringIO()
    sys.stdout = captured_output
    recurse(3)