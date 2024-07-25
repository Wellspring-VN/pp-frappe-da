from base import Base


class SISAttendanceLogCourseClass(Base):
    """
    Class to represent a attendance log course class in SIS system
    """

    ATTRIBUTES = [
        "name",
        "course",
        "course_class",
        "date",
        "direction",
        "period",
        "person_taker",
        "school_year",
        "student_list",
        "timestamp_taken",
        "timetable_day_row_class",
    ]
    doctype = "SIS Attendance Log Course Class"
