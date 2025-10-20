import datetime
import math
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        designation: str = info.get("designation", "")
        name: str = info.get("name", "")
        diameter: float = info.get("diameter", float("nan"))
        hazardous: str = info.get("hazardous", "N")

        self.designation: str = designation
        self.name: str | None = None if name == "" else name
        self.diameter: float = float(diameter) if diameter != "" else float("nan")
        self.hazardous: bool = True if hazardous.upper() == "Y" else False

        # Create an empty initial collection of linked approaches.
        self.approaches: list = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return (
            self.designation
            if self.name is None
            else f"{self.designation} ({self.name})"
        )

    @property
    def details(self) -> str:
        """Return a short detail string for this NEO."""
        name_str = f", '{self.name}'" if self.name is not None else ""
        diameter_str = f", {self.diameter} km" if not math.isnan(self.diameter) else ""
        hazard_str = ", Hazardous" if self.hazardous else ""
        return f"({self.designation}{name_str}{diameter_str}{hazard_str})"

    def __str__(self):
        """Return `str(self)`."""
        diameter = (
            f"diameter of {self.diameter:.3f} km"
            if not math.isnan(self.diameter)
            else "unknown diameter"
        )
        hazard_text = (
            "is potentially hazardous"
            if self.hazardous
            else "is not potentially hazardous"
        )
        return f"NEO {self.fullname} has a {diameter} and {hazard_text}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"
        )

    def serialize(self):
        """Return a dict for CSV/JSON serialization of this close approach."""
        return {
            "designation": self.designation,
            "name": self.name if self.name is not None else "",
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        _designation: str = info.get("designation", "")
        _time: str = info.get("time", "")
        _distance: float = info.get("distance", 0.0)
        _velocity: float = info.get("velocity", 0.0)

        self._designation: str = _designation
        self.time: datetime.datetime = cd_to_datetime(_time)
        self.distance: float = float(_distance) if _distance != "" else float("nan")
        self.velocity: float = float(_velocity) if _velocity != "" else float("nan")

        self.neo = None

    @property
    def time_str(self) -> str:
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        result = f"On {self.time_str}, {self._designation if self.neo is None else self.neo.details}"
        f" approaches Earth at a distance of [{self.distance:.3f} au] and a velocity of [{self.velocity:.3f} km/s]"
        return result

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance:.3f}, "
            f"velocity={self.velocity:.3f}, neo={self.neo!r})"
        )

    def serialize(self):
        """Return a dict for CSV/JSON serialization of this close approach."""
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }


def main():
    o = NearEarthObject(
        designation="2023 AB", name="", diameter="37.675", hazardous="y"
    )
    print(o.designation)
    print(o.name)
    print(o.diameter)
    print(o.hazardous)


if __name__ == "__main__":
    main()
