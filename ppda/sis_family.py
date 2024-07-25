from base import Base


class SISFamily(Base):
    """
    Class to represent a Family in SIS system
    """

    ATTRIBUTES = [
        "name",
        "home_address",
        "status",
        "children",
        "guardians",
    ]
    doctype = "SIS Family"

    def child_exists(self, child_person_id):
        """
        Check if a child exists in the family
        """
        for child in self.children:
            if child["person"] == child_person_id:
                return True
        return False

    def guardian_exists(self, guardian_person_id):
        """
        Check if a guardian exists in the family
        """
        for guardian in self.guardians:
            if guardian["person"] == guardian_person_id:
                return True
        return False
