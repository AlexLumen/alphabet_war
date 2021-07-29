from scr.alphabet_war import alphabet_war


def test_alphabet_war():
    assert alphabet_war("z") == "Right side wins"
    assert alphabet_war("zzzzs") == "Right side wins"
    assert alphabet_war("zdqmwpbs") == "Let's fight again!"
    assert alphabet_war("wwwwwwz") == "Left side wins!"
    assert alphabet_war("") == "Let's fight again!"
