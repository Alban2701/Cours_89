# test_distance_functions.py
import pytest
from exercice import add, sub, mul, div


# --- Tests pour add ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Même unité
        ("500m", "200m", "700m"),
        ("1km", "500m", "1.5km"),
        ("100cm", "50cm", "1.5m"),
        ("1000um", "1000um", "2000um"),
        # Conversions automatiques
        ("500m", "1.6km", "2.1km"),
        ("1m", "99cm", "1.99m"),
        ("1km", "1000m", "2km"),
        ("50cm", "50cm", "1m"),
        # Résultats négatifs
        ("-500m", "300m", "-200m"),
        ("-1km", "-500m", "-1.5km"),
        # Zéro
        ("0m", "500m", "500m"),
        ("1km", "0m", "1km"),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


# --- Tests pour sub ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Même unité
        ("10m", "2m", "8m"),
        ("2m", "10m", "-8m"),
        ("1.5km", "500m", "1km"),
        ("200cm", "50cm", "1.5m"),
        # Conversions automatiques
        ("1km", "500m", "500m"),
        ("500m", "1km", "-500m"),
        ("1000um", "500um", "500um"),
        # Résultats négatifs
        ("500m", "1km", "-500m"),
        ("1m", "2m", "-1m"),
        # Zéro
        ("500m", "500m", "0m"),
        ("1km", "1km", "0m"),
    ],
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected


# --- Tests pour mul ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Multiplication par entier
        ("990m", 3, "2.97km"),
        ("500m", 2, "1km"),
        ("100m", 10, "1km"),
        ("50cm", 2, "1m"),
        # Multiplication par float
        ("1km", 0.5, "500m"),
        ("200m", 0.1, "20m"),
        ("1000um", 1000, "1m"),  # 1000um * 1000 = 1m (1 000 000um → 1m)
        # Résultats négatifs
        ("1km", -2, "-2km"),
        ("-500m", 3, "-1.5km"),
        # Zéro
        ("500m", 0, "0m"),
        ("1km", 0, "0m"),
    ],
)
def test_mul(a, b, expected):
    assert mul(a, b) == expected


# --- Tests pour div ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        # Division par entier
        ("1km", 2, "500m"),
        ("200m", 2, "100m"),
        ("1000m", 10, "100m"),
        ("1m", 100, "1cm"),  # 0.01m → 1cm
        # Division par float
        ("1km", 4, "250m"),
        ("500m", 2.5, "200m"),
        # Résultats négatifs
        ("1km", -2, "-500m"),
        ("-1km", 2, "-500m"),
        # Très petites valeurs
        ("1m", 1000, "1000um"),  # 0.001m = 1000um
        ("1m", 1000000, "1um"),  # 0.000001m = 1um
    ],
)
def test_div(a, b, expected):
    assert div(a, b) == expected


# --- Tests des cas limites ---
def test_zero_values():
    assert add("0m", "0km") == "0m"
    assert sub("0m", "0m") == "0m"
    assert mul("0m", 5) == "0m"
    assert div("0m", 1) == "0m"


def test_very_large_values():
    assert add("1000km", "2000km") == "3000km"
    assert sub("1000000m", "500km") == "500km"  # 1000km - 500km
    assert mul("1km", 1000000) == "1000000km"
    assert div("1000000km", 1000) == "1000km"


def test_very_small_values():
    assert add("1000um", "1000um") == "2000um"
    assert sub("5000um", "2000um") == "3000um"
    assert mul("1um", 1000) == "1000um"  # 1um * 1000 = 1000um
    assert div("1m", 1000000) == "1um"  # 1m / 1000000 = 1um
