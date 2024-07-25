from base import Base


class SISTimetableDay(Base):
    """
    Class to represent a timetable day in SIS system
    """

    ATTRIBUTES = [
        "name",
        "parent",
        "parentfield",
        "parenttype",
        "short_title",
        "timetable_column",
        "title",
        "weekday",
    ]
    doctype = "SIS Timetable Day"
