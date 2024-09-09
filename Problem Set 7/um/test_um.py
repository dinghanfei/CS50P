from um import count

def test_count_boundary():
    assert count('ummmmmmm') == 0
    assert count('yummmy') == 0

def test_count_case():
    assert count('UM') == 1
    assert count('Um,ahhhh') == 1
    assert count('uM,abcd') == 1

def test_count_num():
    assert count('um!') == 1
    assert count('um,hello,world') == 1
