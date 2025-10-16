import pytest
import dataclasses  # Add this import
from university.university import University
from university.constants import UNIVERSITIES



def test_university_creation():
    """Test that all universities in the constants file can be created correctly."""
    for code, name in UNIVERSITIES.items():
        university = University.lookup(code)
        assert university.name == name
        assert university.code == code


def test_invalid_university():
    """Test that an invalid university code raises a ValueError."""
    with pytest.raises(ValueError, match="University 'UNKNOWN' not found."):
        University.lookup("UNKNOWN")


def test_case_insensitive_lookup():
    """Test that lookup works case-insensitively."""
    stanford_lower = University.lookup("stanford")
    stanford_upper = University.lookup("STANFORD")
    assert stanford_lower.name == stanford_upper.name
    assert stanford_lower.code == stanford_upper.code


def test_university_str_representation():
    """Test that the string representation of a university is correct."""
    mit = University.lookup("MIT")
    assert str(mit) == "Massachusetts Institute of Technology (MIT)"


def test_university_immutability():
    """Test that University objects are immutable."""
    mit = University.lookup("MIT")
    with pytest.raises(dataclasses.FrozenInstanceError):
        mit.name = "New Name"


def test_university_equality():
    """Test that two university objects with the same code are equal."""
    mit1 = University.lookup("MIT")
    mit2 = University.lookup("MIT")
    assert mit1 == mit2


def test_university_not_equal():
    """Test that different universities are not considered equal."""
    mit = University.lookup("MIT")
    harvard = University.lookup("HARVARD")
    assert mit != harvard


@pytest.mark.parametrize("invalid_code", ["", " ", "123", "!@#", "waterloo_123", "UoT"])
def test_invalid_university_codes(invalid_code):
    """Test invalid university lookup with different incorrect formats."""
    with pytest.raises(ValueError, match="University '.*' not found."):
        University.lookup(invalid_code)
