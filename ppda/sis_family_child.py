from base import Base


class SISFamilyChild(Base):
    """
    Class to represent a Family Child in SIS system
    """

    ATTRIBUTES = ["name", "person", "notes", "parent"]
    doctype = "SIS Family Child"
