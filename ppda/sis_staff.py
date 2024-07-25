from base import Base


class SISStaff(Base):
    """
    Class to represent a staff in SIS system
    """

    ATTRIBUTES = [
        "name",
        "avatar",
        "employee_code",
        "full_name",
        "person",
    ]
    doctype = "SIS Staff"
