# Créer des fonctions "add" "sub" "mul" "div" pour calculer les
# distances, et trouver trouver l'unité qui permet de
# l'afficher avec le chiffre en unité > 0
# >>> add("500m", "1.6km")
# "2.1km"
# >>> sub("2m", "10m")
# "-8m"
# >>> div("1km", 2)
# "500m"
# >>> mul("990m", 3)
# "2.97km"
# unitées disponibles : km ; m ; cm ; µm

KM_UM = 1000000000
M_UM = 1000000
CM_UM = 10000


def int_or_float(num: float) -> int | float:
    if num.is_integer():
        return int(num)
    else:
        return num


def from_km_to_microm(distance: str) -> str:
    num = float(distance.removesuffix("km"))
    num *= KM_UM
    return f"{int_or_float(num)}m"


def from_cm_to_microm(distance: str) -> str:
    num = float(distance.removesuffix("cm"))
    num *= CM_UM
    return f"{int_or_float(num)}m"


def from_microm_to_m(distance: str) -> str:
    num = float(distance.removesuffix("um"))
    num /= M_UM
    return f"{int_or_float(num)}m"


def from_microm_to_km(distance: str) -> str:
    num = float(distance.removesuffix("um"))
    num /= KM_UM
    return f"{int_or_float(num)}km"


def from_microm_to_cm(distance: str) -> str:
    num = float(distance.removesuffix("um"))
    num /= CM_UM
    return f"{int_or_float(num)}cm"


def from_m_to_microm(distance: str) -> str:
    num = float(distance.removesuffix("m"))
    num *= M_UM
    return f"{int_or_float(num)}um"


def convert_to_micrometer(distance: str) -> str:
    if "km" in distance:
        return from_km_to_microm(distance)
    elif "cm" in distance:
        return from_cm_to_microm(distance)
    elif "um" in distance:
        return distance
    else:
        return from_m_to_microm(distance)


def get_numeric_part(distance: str) -> int | float:
    numeric_part = ""
    for char in distance:
        if char.isdigit() or char in ["-", "."]:
            numeric_part += char

    num = float(numeric_part)
    return int_or_float(num)


def get_best_unit(num_distance: float | int) -> str:
    if abs(num_distance) >= KM_UM:
        return from_microm_to_km(f"{num_distance}um")
    elif abs(num_distance) >= M_UM or num_distance == 0:
        return from_microm_to_m(f"{num_distance}um")
    elif abs(num_distance) >= CM_UM:
        return from_microm_to_cm(f"{num_distance}um")
    else:
        return f"{int_or_float(num_distance)}um"


def add(*args: str) -> str:
    total = 0
    for arg in args:
        arg = convert_to_micrometer(arg)
        total += get_numeric_part(arg)

    return get_best_unit(total)


def sub(*args: str) -> str:
    first = True
    for arg in args:
        arg = convert_to_micrometer(arg)

        if first:
            total = get_numeric_part(arg)
            first = False

        else:
            total -= get_numeric_part(arg)

    return get_best_unit(total)


def mul(distance: str, multiplier: float) -> str:
    distance = convert_to_micrometer(distance)
    num = get_numeric_part(distance)
    total = num * multiplier
    return get_best_unit(total)


def div(distance: str, divider: float) -> str:
    distance = convert_to_micrometer(distance)
    num = get_numeric_part(distance)
    total = num / divider
    return get_best_unit(total)
