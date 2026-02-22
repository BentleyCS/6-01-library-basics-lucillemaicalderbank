import pytest
# This must match your filename 'CSP_6_01_Library_Basics.py'
from CSP_6_01_Library_Basics import search_and_report


def test_search_and_report(monkeypatch):
    # 1. Setup data
    test_list = ["  Banana", "APPLE", "  cherry  "]

    # 2. Mock the input to simulate user typing "apple"
    monkeypatch.setattr('builtins.input', lambda _: "apple")

    # 3. Run the function
    result = search_and_report(test_list)

    # 4. Assert the result (APPLE cleaned is at index 1)
    assert result == 1


def test_search_not_found(monkeypatch):
    test_list = ["apple", "banana"]
    monkeypatch.setattr('builtins.input', lambda _: "dragonfruit")

    result = search_and_report(test_list)
    assert result == -1
