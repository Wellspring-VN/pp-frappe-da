from base import Base


class SISTimetableColumnRow(Base):
    """
    Class to represent a timetable column row in SIS system
    """

    ATTRIBUTES = [
        "name",
        "parent",
        "parentfield",
        "parenttype",
        "short_title",
        "time_end",
        "time_start",
        "title",
        "type",  # ["Lesson", "Break", "Lunch", "Other"]
    ]
    doctype = "SIS Timetable Column Row"
