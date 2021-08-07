# Schedule with and ID number and list of sections
class Schedule:
    def __init__(self, id, sections):
        self.id = id
        self.sections = sections


# Course with its list of sections
class Course:
    def __init__(self, name, sections):
        self.name = name
        self.sections = sections


# Section of a course with an ID number and list of meeting times
class Section:
    def __init__(self, id, classes):
        self.id = id
        self.classes = classes


# Description of a time when a certain course meets
class MeetingTime:
    def __init__(self, weekday, timeperiod):
        self.weekday = weekday
        self.timeperiod = timeperiod


# Period of Time in Military Notation
class TimePeriod:
    def __init__(self, start, end):
        self.start = start
        self.end = end
