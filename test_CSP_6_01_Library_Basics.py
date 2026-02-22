
from CSP_6_01_Library_Basics import search_and_report


def test_search_and_report(monkeypatch):
    test_list = ["  Banana", "APPLE", "  cherry  "]

    monkeypatch.setattr('builtins.input', lambda _: "apple")

    result = search_and_report(test_list)

    assert result == 1


def test_search_not_found(monkeypatch):
    test_list = ["apple", "banana"]
    monkeypatch.setattr('builtins.input', lambda _: "dragonfruit")

    result = search_and_report(test_list)
    assert result == -1
