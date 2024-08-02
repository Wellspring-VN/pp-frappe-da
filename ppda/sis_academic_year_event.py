from base import Base


class SISAcademicYearEvent(Base):
    """
    Class to represent a academic year event in SIS system
    """

    ATTRIBUTES = [
        "name",
        "description",
        "enable",
        "end_date",
        "school_year",
        "start_date",
        "title",
    ]
    doctype = "SIS Academic Year Event"
