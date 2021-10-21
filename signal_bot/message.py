class Message:
    """Message class to model data."""

    def __init__(self, source, message, groupinfo, timestamp):
        """Initialize Message object with source, message and groupinfo."""
        self._source = source
        self._message = message
        self._groupinfo = groupinfo
        self._timestamp = timestamp

    def getgroupinfo(self):
        """Return groupID."""
        return self._groupinfo

    def getmessage(self):
        """Return message string."""
        return self._message

    def getsource(self):
        """Return source string."""
        return self._source

    def gettimestamp(self):
        """Return timestamp string."""
        return str(self._timestamp)