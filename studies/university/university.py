from dataclasses import dataclass
from .constants import UNIVERSITIES

@dataclass(frozen=True)
class University:
    """
    Represents a university with a unique code and name.

    Attributes:
        code (str): Short code for the university.
        name (str): Full university name.
    """
    code: str
    name: str

    @classmethod
    def lookup(cls, code: str):
        """Creates a University object from a given code."""
        code = code.upper()
        if code not in UNIVERSITIES:
            raise ValueError(f"University '{code}' not found.")
        return cls(code, UNIVERSITIES[code])

    def __str__(self):
        return f"{self.name} ({self.code})"