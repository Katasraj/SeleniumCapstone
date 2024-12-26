'''To handle both scripts and interactive environments'''


from pathlib import Path
import os

class FileLocation:
    def csv_location(self):
        try:
            # Script environment
            BASE_DIR = Path(__file__).parent
        except NameError:
            # Interactive environment
            BASE_DIR = Path.cwd()


        courses_prices = BASE_DIR / "testdata.csv"
        courses = BASE_DIR / "drop_down_courses.csv"

        return [courses_prices,courses]
# print(courses)
# print(courses_prices)

# f = FileLocation()
#print(FileLocation().csv_location()[0])