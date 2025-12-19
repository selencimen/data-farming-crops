# pylint: disable=too-few-public-methods


class Crop:
    """
    Base class for all crops.
    Handles common grain logic.
    """

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True if crop is ripe."""
        return self.grains >= 15
