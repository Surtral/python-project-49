from brain_games.scripts.brain_games import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Welcome to the Brain Games!" in captured.out
