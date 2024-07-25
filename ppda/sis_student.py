from base import Base


class SISStudent(Base):
    """
    Class to represent a student in SIS system
    """

    ATTRIBUTES = [
        "name",
        "person",
        "wellspring_student_code",
    ]
    doctype = "SIS Student"
