from base import Base


class SISClassFeed(Base):
    """
    Class to represent a class feed in SIS system
    """

    ATTRIBUTES = [
        "name",
        "content",
        "description",
        "photos",  # [SISClassFeedPhoto]
        "public_time",
        "school_class",
        "status",  # ["Draft", "Waiting Approval", "Public"]
        "title",
    ]
    doctype = "SIS Class Feed"
