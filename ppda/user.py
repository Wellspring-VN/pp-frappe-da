from base import Base


class User(Base):
    """
    Class to represent a user in SIS system
    """

    ATTRIBUTES = ["name", "first_name", "last_name", "email", "password"]
    doctype = "User"
