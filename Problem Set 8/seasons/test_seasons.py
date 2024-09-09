from datetime import date
from seasons import get_delta

def test_get_delta():
    assert get_delta(date(2002, 11, 27), date(2002, 11, 27)) == 0
    assert get_delta(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert get_delta(date(2001, 1, 1), date(2003, 1, 1)) == 1051200


