from sistema import somar
from sistema import subtrair
from sistema import multiplicar
from sistema import dividir

def test_somar():
    # Estamos afirmando que:
    # 2 + 3 deve producir 5.
    assert somar (2, 3) == 5

def test_subtrair():
    # Estamos afirmando que:
    # 20 - 15 deve producir 5.
    assert subtrair (20, 15) == 5

def test_mustiplicar():
    # Estamos afirmando que:
    # 5 * 7 deve producir 35.
    assert multiplicar (5, 7) == 35

def test_dividir():
    # Estamos afirmando que:
    # 20 / 4 deve proucir 5.
    assert dividir (20, 4) == 5