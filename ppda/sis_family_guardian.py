from base import Base


class SISFamilyGuardian(Base):
    """
    Class to represent a Family Guardian in SIS system
    """

    ATTRIBUTES = [
        "name",
        "person",
        "relationship_with_student",
        "notes",
        "child_data_access",
        "parent",
    ]
    doctype = "SIS Family Guardian"
