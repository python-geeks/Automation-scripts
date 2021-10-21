import functions


class SwitchCase(
    functions.Help, functions.Bored, functions.Chuck, functions.Dog, functions.Flip, functions.Gif,
    functions.Gnews, functions.Haiku, functions.Hn, functions.Me, functions.Rand, functions.Test,
    functions.Trivia, functions.Twitch, functions.Version, functions.Winamp, functions.TestEmoji,
    functions.Xkcd, functions.Tmdb
):
    """SwitchCase class to switch bot functions."""

    def __init__(self, version, author, signalexecutorlocal, messageobject):
        """Initialize SwitchCase with version, author, signalexecutor and the messagestring."""
        self._version = version
        self._author = author
        self._signalexecutorlocal = signalexecutorlocal
        self._messageobject = messageobject

    def switch(self, action):
        """Switch function to switch between available functions."""
        default = "Invalid option."
        return getattr(self, str(action)[1:].split()[0], lambda: default)()