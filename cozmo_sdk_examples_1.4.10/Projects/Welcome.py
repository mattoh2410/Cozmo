import datetime

import cozmo

"class to deal with all the speach"


class Welcome:
    def cozmo_program(robot:):

    def __init__(self, robot, weather):
        self.robot = robot
        self.time = x = datetime.datetime.now()
        self.hour = self.time.strftime("%I")
        self.min = self.time.strftime("%M")
        self.day = self.time.strftime("%A")
        self.day_no = self.time.strftime("%d")
        self.month = self.time.strftime("%B")

    def set_date(self):
        if self.day_no == 1:
            self.day_no = "1st"
        elif self.day_no == 21:
            self.day_no = "21st"
        elif self.day_no == 2:
            self.day_no = "2nd"
        elif self.day_no == 22:
            self.day_no = "22nd"
        elif self.day_no == 3:
            self.day_no = "3rd"
        elif self.day_no == 23:
            self.day_no = "23rd"
        elif self.day_no == 31:
            self.day_no = "31st"
        else:
            self.day_no = self.day_no + "th"

    def welcome_afternoon(self, name):
        print("in", city, "there will be highs of", w.get_temperature('celsius')['temp_max'], "and lows of",
              w.get_temperature('celsius')['temp_min'], "with an avg of", w.get_temperature('celsius')['temp'])
        self.robot.say_text("Good afternoon", name)
        self.robot.say_text(" It is currently ", self.hour, self.min, "on", self.day, "the", self.day_no, "of",
                            self.month)
