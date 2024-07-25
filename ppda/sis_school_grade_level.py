from base import Base


class SISSchoolGradeLevel(Base):
    """
    Class to represent a grade level in SIS system
    """

    ATTRIBUTES = [
        "name",
        "title",
        "short_title",
        "sequence_number",
    ]
    doctype = "SIS School Grade Level"
