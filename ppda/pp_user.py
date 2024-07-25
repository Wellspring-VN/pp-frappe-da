from base import Base


class PPUser(Base):
    """
    Class to represent a PP user in SIS system
    """

    ATTRIBUTES = [
        "name",
        "enabled",
        "first_name",
        "full_name",
        "person",
        "sis_role",  # ["Parent", "Teacher", "Admin"]
        "user",
        "user_image",
    ]
    doctype = "PP User"
