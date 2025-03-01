import f3_choose_team
import pytest

def test_f3_chooseSportsTeam_menu(monkeypatch, capsys):
    # Mock input to simulate user selecting the first team
    monkeypatch.setattr('builtins.input', lambda _: "3")

    # Call the function
    f3_choose_team.choose_sports_team()
    
    # Capture the output
    captured = capsys.readouterr()

    # Verify the printed menu
    assert "[1] BYU" in captured.out
    assert "[2] UVU" in captured.out
    assert "[3] USU" in captured.out
    assert "[4] SUU" in captured.out
    assert "[5] UofU" in captured.out

def test_f3_chooseSportsTeam_homeTeam_min(monkeypatch, capsys):
    # Mock input to simulate user selecting the first team
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # Call the function
    selected_team = f3_choose_team.choose_sports_team()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the selected team
    assert selected_team == "BYU"

def test_f3_chooseSportsTeam_homeTeam_max(monkeypatch, capsys):
    # Mock input to simulate user selecting the last team
    monkeypatch.setattr('builtins.input', lambda _: "5")

    # Call the function
    selected_team = f3_choose_team.choose_sports_team()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the selected team
    assert selected_team == "UofU"

def test_f3_chooseSportsTeam_awayTeam_menu(monkeypatch, capsys):
    # Mock input to simulate user selecting the first team
    monkeypatch.setattr('builtins.input', lambda _: "3")
    home_team = "BYU"

    # Call the function
    f3_choose_team.choose_sports_team(home_team)
    
    # Capture the output
    captured = capsys.readouterr()

    # Verify the printed menu
    assert "[1] BYU" not in captured.out
    assert "[1] UVU" in captured.out
    assert "[2] USU" in captured.out
    assert "[3] SUU" in captured.out
    assert "[4] UofU" in captured.out

def test_f3_chooseSportsTeam_awayTeam_min(monkeypatch, capsys):
    # Mock input to simulate user selecting the first team
    monkeypatch.setattr('builtins.input', lambda _: "1")
    home_team = "BYU"

    # Call the function
    selected_team = f3_choose_team.choose_sports_team(home_team)

    # Capture the output
    captured = capsys.readouterr()

    # Verify the selected team
    assert selected_team == "UVU"

def test_f3_chooseSportsTeam_awayTeam_max(monkeypatch, capsys):
    # Mock input to simulate user selecting the first team
    monkeypatch.setattr('builtins.input', lambda _: "4")
    home_team = "UofU"

    # Call the function
    selected_team = f3_choose_team.choose_sports_team(home_team)

    # Capture the output
    captured = capsys.readouterr()

    # Verify the selected team
    assert selected_team == "SUU"