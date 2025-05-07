"""

python3 core8/pwb.py newapi/tests/test_bot_edit

"""
from newapi.page import MainPage

# ---
titles = [
    "جبل عمر",
    "ويكيبيديا:ملعب",
    "القدس_خلال_فترة_الهيكل_الثاني"
]
# ---
for x in titles:
    page = MainPage(x, "ar")

    canedit = page.can_edit(delay=10)

    print(f"Page: {x}, \t:{canedit=}")
