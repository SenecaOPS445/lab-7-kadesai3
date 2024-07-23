#!/usr/bin/env python3
# Student ID: kadesai3
# lab7h.py

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __repr__(self):
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return Time(hours, minutes, seconds)

if __name__ == "__main__":
    t1 = Time(1, 30, 15)
    t2 = Time(2, 45, 30)
    print(f"t1: {t1}")
    print(f"t2: {t2}")
    print(f"t1 + t2: {t1 + t2}")
    print(f"t2 - t1: {t2 - t1}")
    print(f"t1 == t2: {t1 == t2}")
    print(f"t1 < t2: {t1 < t2}")
