from base import Base


class SISCourse(Base):
    """
    Class to represent a course in SIS system
    """

    ATTRIBUTES = [
        "name",
        "description",
        "program_type",
        "short_title",
        "title",
    ]
    doctype = "SIS Course"
