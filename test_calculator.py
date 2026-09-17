import pytest
from calculator import add, subtract, multiply, divide, parse_input, repl

def test_math_operations():
    assert add(10.5, 4.5) == 15.0
    assert subtract(100, 40) == 60
    assert multiply(5, 5) == 25
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(100, 0)

def test_repl_exit(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    repl()
    assert "Goodbye!" in capsys.readouterr().out
