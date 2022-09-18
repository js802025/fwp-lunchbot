###
###  FWP lunch menu parser
###  By Jake B
###  Original Sep 2019, improved Oct 2019, improved & class-ified Nov 2021
###

import string
import pdftotext
from six.moves.urllib.request import urlopen
import io
import sys
import camelot


class Lunchbot:
    def __init__(self, url):
        # Getting the lunch menu PDF and putting it into a variable
        #remote_file = urlopen(url).read()
        #memory_file = io.BytesIO(remote_file)
        #pdf = pdftotext.PDF(memory_file)
        pdf = camelot.read_pdf(url)
        self.pdf_content = pdf[0]


        # Creating dictionary to hold the location of each day's meal list in the list
        self.dict = {"Monday:": 0, "Tuesday:": 0, "Wednesday:": 0, "Thursday:": 0, "Friday:": 0}
        self.days_of_the_week = ["Mon", "Tues", "Wednes", "Thurs", "Fri"]

        self.parse_pdf()


    def parse_pdf(self):
        # This function parses the PDF and puts the menu into a dictionary of days of the week and their respective lunch menus.

        self.menu = {}



        # for index, item in enumerate(text):
        #     dayLunch = item.split("\n")[1:-1]
        #     if not index == 0:
        #         self.menu[dayName+ "day"] = "\n".join(dayLunch)
        #     dayName = item.split("\n")[-1]
        for col in self.pdf_content.df:
            for row in self.pdf_content.df[col]:
                if "day" in row:
                    row_lines = row.split("\n")
                    dayName = row_lines[0].split("day:")[0]+"day"
                    lunch = "\n".join(row_lines[1:]).replace("\n•", "").replace("•", "")
                    self.menu[dayName] = lunch



    def get_week(self):
        #print(self.pdf_content)
        #compiles all the days of the week into one message bc we aren't that rich here.
        week_menu = ""
        for day in self.days_of_the_week:
            week_menu += day+"day"+":\n"+self.menu[day+"day"]+"\n\n"
        #print(week_menu)

        return week_menu#.replace("(", "").replace(")", "").replace("/", "").replace(":", "")


    def get_day(self, day):
        # Improved version of the old get_day function. Simply returns the lunch menu for the day requested.

        return self.menu[day+"day"]


if __name__ == '__main__':

    # This method is outdated, use lunch_parser cached menus

    day_requested = "T"
    url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf'

    bot = Lunchbot(url)

    todays_menu = bot.get_week()
    print(todays_menu)
