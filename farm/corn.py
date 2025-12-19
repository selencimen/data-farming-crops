from farm.crop import Crop


class Corn(Crop):
    """
    Corn crop implementation.
    """

    def water(self):
        """Add grains by watering corn."""
        self.grains += 10

