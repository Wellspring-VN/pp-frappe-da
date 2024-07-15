from base import Base


class User(Base):
    """
    Class to represent a user in SIS system
    """

    ATTRIBUTES = ["name", "full_name", "email"]
    doctype = "User"
