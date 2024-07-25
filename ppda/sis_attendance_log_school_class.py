from base import Base


class SISAttendanceLogSchoolClass(Base):
    """
    Class to represent a attendance log school class in SIS system
    """

    ATTRIBUTES = [
        "name",
        "date",
        "direction",
        "person_taker",
        "school_class",
        "school_year",
        "student_list",
        "timestamp_taken",
    ]
    doctype = "SIS Attendance Log School Class"
