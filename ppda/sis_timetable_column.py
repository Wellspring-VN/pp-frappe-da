from base import Base


class SISTimetableColumn(Base):
    """
    Class to represent a timetable column in SIS system
    """

    ATTRIBUTES = [
        "name",
        "short_title",
        "timetable_column_row",
        "title",
    ]
    doctype = "SIS Timetable Column"
