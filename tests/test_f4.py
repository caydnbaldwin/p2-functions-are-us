import pytest
import f4_wins_losses

def test_f4_winLoseSim_W(monkeypatch):
    # force home team win
    scores = [5, 3]
    def mock_randint(start, end):
        return scores.pop(0)
    monkeypatch.setattr("random.randint", mock_randint)
    result = f4_wins_losses.winLoseSim()
    assert result == 'W', f"Expected 'W' but got {result}"

def test_f4_winLoseSim_L(monkeypatch):
    # force home team win
    scores = [3, 5]
    def mock_randint(start, end):
        return scores.pop(0)
    monkeypatch.setattr("random.randint", mock_randint)
    result = f4_wins_losses.winLoseSim()
    assert result == 'L', f"Expected 'L' but got {result}"