from base import Base


class SISSchoolClass(Base):
    """
    Class to represent a school class in SIS system
    """

    ATTRIBUTES = [
        "name",
        "school_year",
        "school_grade_level",
        "title",
        "short_title",
        "participants",
    ]
    doctype = "SIS School Class"
