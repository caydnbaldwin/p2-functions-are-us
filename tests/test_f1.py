import f1_introduction
import pytest

def test_f1_display_intro_introduction(monkeypatch, capsys):
    # Mock input to simulate user entering their name
    monkeypatch.setattr('builtins.input', lambda _: "TestUser")

    # Call the function
    f1_introduction.display_intro()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the printed introduction
    assert "Welcome to the College Soccer Season Simulator!" in captured.out
    assert "In this game, you will coach a soccer team through a season." in captured.out
    assert "You will enter your team's name, choose the number of games to play (1-10)," in captured.out
    assert "and input the opponents' names. Scores will be randomly generated." in captured.out
    assert "Your goal is to win as many games as possible and qualify for the NCAA Tournament!" in captured.out

def test_f1_display_intro_username(monkeypatch, capsys):
    # Mock input to simulate user entering their name
    monkeypatch.setattr('builtins.input', lambda _: "TestUser")

    # Call the function
    f1_introduction.display_intro()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the printed output
    assert "Great to have you here, Coach TestUser!" in captured.out

def test_f4_display_intro_return(monkeypatch):
    # Mock input to simulate user entering their name
    monkeypatch.setattr('builtins.input', lambda _: "TestUser")

    # Call the function and capture the return value
    user_name = f1_introduction.display_intro()

    # Verify the return value
    assert user_name == "TestUser"