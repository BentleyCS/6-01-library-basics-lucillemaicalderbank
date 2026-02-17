import builtins
import main


def test_process_expenses():
    assert main.process_expenses([100, 200]) == [115.0, 230.0]


def test_sanitize_usernames():
    data = ["  Alice ", "BOB", " ChArLiE  "]
    assert main.sanitize_usernames(data) == ["alice", "bob", "charlie"]


def test_identify_outliers():
    data = [50, 150, 200, 75]
    assert main.identify_outliers(data) == [150, 200]


def test_analyze_scores(monkeypatch):
    inputs = iter(["90", "80", "100"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    highest, avg = main.analyze_scores(3)

    assert highest == 100
    assert avg == 90.0


def test_search_and_report_sorted(monkeypatch):
    items = ["  Apple", "Banana ", "  CHERRY  ", " date "]

    monkeypatch.setattr(builtins, "input", lambda _: "banana")

    result = main.search_and_report(items)

    assert "Found at index" in result
