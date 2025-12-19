from farm.crop import Crop


class Rice(Crop):
    """
    Rice crop implementation.
    """

    def water(self):
        """Add grains by watering rice."""
        self.grains += 5

    def transplant(self):
        """Transplant rice to add extra grains."""
        self.grains += 10
