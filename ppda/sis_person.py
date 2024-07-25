from base import Base


class SISPerson(Base):
    """
    Class to represent a person in SIS system
    """

    ATTRIBUTES = [
        "name",
        "avatar",
        "common_name",
        "date_of_birth",
        "email",
        "english_name",
        "first_name",
        "full_name",
        "gender",
        "last_name",
        "middle_name",
        "nationality",
        "phone_number",
        "primary_role",  # ["Student", "Guardian", "Teacher", "Staff"]
    ]
    doctype = "SIS Person"
