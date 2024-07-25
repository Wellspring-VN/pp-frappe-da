from base import Base


class SISSchoolYear(Base):
    """
    Class to represent a school year in SIS system
    """

    ATTRIBUTES = [
        "name",
        "title",
        "status",
        "first_day",
        "last_day",
        "sequence_number",
    ]
    doctype = "SIS School Year"
