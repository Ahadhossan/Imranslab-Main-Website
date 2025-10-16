# instructor/instructor.py
from dataclasses import dataclass, field
from typing import List, Optional
from university.university import University

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

    def __str__(self):
        return f"{self.name}, {self.university.name} - Area: {self.area_of_interest}"