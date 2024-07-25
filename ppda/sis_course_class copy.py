from base import Base


class SISCourseClass(Base):
    """
    Class to represent a course class in SIS system
    """

    ATTRIBUTES = [
        "name",
        "attendance",
        "class_type",
        "course",
        "enrollment_max",
        "enrollment_min",
        "participants",
        "school_year",
        "short_title",
        "timetable",
        "timetable_day_row_class",
        "title",
    ]
    doctype = "SIS Course Class"
