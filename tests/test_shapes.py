import pytest
from geometria import(
	area_rectangulo,
	area_circulo,
	area_triangulo,
	volumen_paralelepipedo,
        volumen_cono,
        volumen_esfera,
)

def test_area_rectangulo():
	assert area_rectangulo(4, 5) == 20

def test_area_triangulo():
	assert area_triangulo(10, 6) == 30

def test_area_circulo():
	assert area_circulo(1) == pytest.approx(3.1416, rel=1e-3)

def test_volumen_paralelepipedo():
	assert volumen_paralelepipedo(2, 3, 4) == 24

def test_volumen_cono():
	assert volumen_cono(1, 3) == pytest.approx(3.1416, rel=1e-3)

def test_volumen_esfera():
	assert volumen_esfera(1) == pytest.approx(4.1888, rel=1e-3)

