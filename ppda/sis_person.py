from base import Base


class SISPerson(Base):
    """
    Class to represent a person in SIS system
    """

    ATTRIBUTES = [
        "name",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "gender",
        "nationality",
        "date_of_birth",
    ]
    doctype = "SIS Person"
