import datetime
import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        
            
        for line in self.file:
            second, color, created= line.strip().split(";")
            self.users[second] = (color, created)
        self.file.close()

    def get_user(self, second):
        return self.users[second]

    def add_user(self, second, color):
        self.users[second.strip()] = (color.strip(), DataBase.get_date())
        self.save()
        
    def validate(self, second, color):
        if self.get_user(second) != -1:
            return self.users[second][0] == color
    

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
