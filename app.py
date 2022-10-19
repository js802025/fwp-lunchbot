from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
from lunch_menu_parser import Lunchbot

import requests

app = Flask(__name__)

##remote_menu_url = "http://fwp-lunchbot.s3.us-east-2.amazonaws.com/menu.txt" this never needed to exist

bot = Lunchbot("https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf")

##def read_parsed_text_menu():
##    "Read contents of remote menu file."
##    remote_menu = requests.get(remote_menu_url)
##    remote_menu.encoding = remote_menu.apparent_encoding
##    return(remote_menu.text.strip())
from_numbers = {}

@app.route('/sms', methods=['POST'])
def sms():

    # number = request.form['From'] # variable not needed
    # message_body = request.form['Body'].title().strip() # Who cares
    if request.form['From'] in from_numbers.keys():
        from_numbers[request.form['From']] += 1
    else:
        from_numbers[request.form['From']] = 1
    print(from_numbers)
    if from_numbers[request.form['From']] <= 3:
        resp = MessagingResponse()
        response = bot.get_week()+"\nSponsered by CTC & FTC Robotics"
        resp.message(response)
        return str(resp)

if __name__ == '__main__':
    app.run()

    # from datetime import date
    # import sys
    # today = date.today().strftime('%A')
    # message_body = sys.argv[1]

    # days_of_the_week = ["M", "T", "W", "Th", "F"]
    # if message_body in days_of_the_week: # If the message is something we know how to do
    #     todays_menu = read_menu(message_body)
    # elif today[0] in days_of_the_week or today[0:1] in days_of_the_week: # Tuesday and Thursday
    #     if today == "Thursday":
    #         todays_menu = read_menu("Th")
    #     else:
    #         todays_menu = read_menu(today[0])
    # else:
    #     todays_menu = read_menu("M")
    # print(todays_menu + '\n \nSponsored by CTC/Student Government & FTC Robotics')
