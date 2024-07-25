from base import Base


class SISTimetable(Base):
    """
    Class to represent a timetable in SIS system
    """

    ATTRIBUTES = [
        "name",
        "grade_level_list",
        "school_year",
        "short_title",
        "status",
        "timetable_days",
        "title",
    ]
    doctype = "SIS Timetable"
