import requests
from typing import Union

URL = "https://www.hebcal.com/converter?cfg=json&"


# ========= main func ============
def convert(
        day: int,
        month: Union[str, int],
        year: int,
        to_hebrew: bool = True) -> dict:
    url = URL
    flag = "g" if not to_hebrew else "h"
    url += f"{flag}y={year}&{flag}m={month}&{flag}d={day}&"
    url += "h2g=1"
    return requests.get(url).json()


# ======= months ===========
he_month = {"Nisan": ["ניסן"],
            "Iyyar": ["אייר", "איר"],
            "Sivan": ["סיוון", "סיון"],
            "Tamuz": ["תמוז"],
            "Av": ["אב"],
            "Elul": ["אלול"],
            "Tishrei": ["תשרי", "תישרי"],
            "Cheshvan": ["חשוון", "חשון", "מרחשוון", "מר-חשון"],
            "Kislev": ["כסלו", "כיסליו", "כסליו", "כיסלו"],
            "Tevet": ["טבת"],
            "Shvat": ["שבט"],
            "Adar1": ["אדר"],
            "Adar2": ["אדר ב'", "אדר ב"]}


def return_month(month: str) -> Union[str, bool]:
    """
    from [חשוון] to Cheshvan
    """
    for m_en in he_month:
        if month in he_month[m_en]:
            return m_en

    else:
        return False


# ======== days ============
he_days = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "יא": 11,
    "יב": 12,
    "יג": 13,
    "יד": 14,
    "טו": 15,
    "טז": 16,
    "יז": 17,
    "יח": 18,
    "יט": 19,
    "כ": 20,
    "כא": 21,
    "כב": 22,
    "כג": 23,
    "כד": 24,
    "כה": 25,
    "כו": 26,
    "כז": 27,
    "כח": 28,
    "כט": 29,
    "ל": 30
}


def return_day(day: str) -> Union[str, int, bool]:
    """
    from [כ"א, ט"ו, י'] to [21, 15, 10]
    """
    day = day.replace('"', "").replace("''", "").replace("'", "")

    for _day in he_days:
        if day == _day:
            return he_days[_day]

    else:
        return False


# ======== years ============

he_years = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,

    "כ": 20,
    "ל": 30,
    "מ": 40,
    "נ": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "צ": 90
}


def return_year(year: str) -> Union[bool, int]:
    """
    from [תשל"ח, תש"פ] to [5738, 5780]
    """
    year = year.replace("תש", "").replace('"', "").replace("'", "")

    if not year:
        return False

    gi = he_years.get(year[0])  # second example
    if gi:

        if len(year) > 1:  # taking care of first example
            gi2 = he_years.get(year[1])
            if gi2 and gi2 < 10:
                year_int = int(gi) + int(gi2)
            else:
                return False

        else:
            year_int = int(gi)

        return year_int + 5700

    else:
        return False
