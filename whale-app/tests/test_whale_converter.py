from src.whale_converter import make_whale_sound, to_whale_speak


def test_to_whale_speak_basic():
    assert to_whale_speak("hello") == "hll"


def test_to_whale_speak_with_capitals():
    assert to_whale_speak("HeLLo WOrld") == "HLL Wrld"


def test_to_whale_speak_empty():
    assert to_whale_speak("") == ""


def test_to_whale_speak_no_vowels():
    assert to_whale_speak("rhythm") == "rhythm"


def test_to_whale_speak_only_vowels():
    assert to_whale_speak("aeiou") == ""


def test_to_whale_speak_special_chars():
    assert to_whale_speak("hello!@#$%") == "hll!@#$%"


def test_make_whale_sound():
    assert make_whale_sound(1) == "Oooo"
    assert make_whale_sound(2) == "OOoooooo"
    assert make_whale_sound(3) == "OOOooooooooo"
    try:
        make_whale_sound(4)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
