from dataclasses import dataclass, field
from typing import List, Optional
from university.university import University
from .constants import INSTRUCTORS

@dataclass(frozen=True)
class Instructor:
    """
    Represents an instructor with personal and professional details.

    Attributes:
        name (str): Full name of the instructor.
        number (str): Contact number.
        email (str): Email address.
        area_of_interest (str): Primary research and teaching interests.
        university (University): Associated university object.
        publications (List[str]): List of publication links or file paths.
        website (Optional[str]): Personal or professional website link.
    """
    name: str
    number: str
    email: str
    area_of_interest: str
    university: University
    publications: List[str] = field(default_factory=list)
    website: Optional[str] = None

    @classmethod
    def lookup(cls, code: str):
        """Creates an Instructor object from a given code."""
        code = code.upper()
        if code not in INSTRUCTORS:
            raise ValueError(f"Instructor '{code}' not found.")
        data = INSTRUCTORS[code]
        university = University.lookup(data["university"])
        return cls(
            name=data["name"],
            number=data["number"],
            email=data["email"],
            area_of_interest=data["area_of_interest"],
            university=university,
            publications=data["publications"],
            website=data["website"]
        )

    def __str__(self):
        return f"{self.name}, {self.university.name} - Area: {self.area_of_interest}"