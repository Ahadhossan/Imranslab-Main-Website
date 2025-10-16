# tests/tools/test_validators.py

"""
Unit tests for DirectoryValidator in synthetic_data_factory/tools/validators.py
"""
import pytest
from pathlib import Path

from test_data.synthetic_data.synthetic_data_factory.tools.validators.validators import DirectoryValidator


def test_valid_directory(tmp_path: Path):
    """
    DirectoryValidator should accept an existing directory without raising.
    """
    # tmp_path is a built-in pytest fixture providing a Path to a temp directory
    DirectoryValidator(tmp_path)  # Should not raise any exception


def test_nonexistent_directory(tmp_path: Path):
    """
    DirectoryValidator should raise ValueError for a non-existing path.
    """
    fake_dir = tmp_path / "no_such_folder"
    with pytest.raises(ValueError) as excinfo:
        DirectoryValidator(fake_dir)
    assert f"Not a directory: {fake_dir}" in str(excinfo.value)


def test_file_instead_of_directory(tmp_path: Path):
    """
    DirectoryValidator should raise ValueError when given a file path.
    """
    # Create a temporary file
    file_path = tmp_path / "a_file.txt"
    file_path.write_text("dummy content")
    with pytest.raises(ValueError) as excinfo:
        DirectoryValidator(file_path)
    assert f"Not a directory: {file_path}" in str(excinfo.value)


def test_relative_path_accepts_cwd(tmp_path: Path, monkeypatch):
    """
    DirectoryValidator should handle relative paths by resolving them.
    """
    # Change current working directory to tmp_path
    monkeypatch.chdir(tmp_path)
    validator = DirectoryValidator(Path("."))
    assert validator.path == tmp_path.resolve()


def test_resolved_path_property(tmp_path: Path):
    """
    DirectoryValidator.path attribute should store the resolved absolute path.
    """
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    validator = DirectoryValidator(subdir)
    assert isinstance(validator.path, Path)
    assert validator.path == subdir.resolve()


import os

@pytest.mark.skipif(not hasattr(os, 'symlink'), reason="OS does not support symlinks")
def test_symlink_to_directory(tmp_path: Path):
    """
    DirectoryValidator should accept a symlink pointing to a valid directory.
    """
    real_dir = tmp_path / "real_dir"
    real_dir.mkdir()
    link = tmp_path / "link_dir"
    link.symlink_to(real_dir)
    validator = DirectoryValidator(link)
    # Path.resolve() follows symlink
    assert validator.path == real_dir.resolve()

@pytest.mark.skipif(not hasattr(os, 'symlink'), reason="OS does not support symlinks")
def test_dangling_symlink(tmp_path: Path):
    """
    DirectoryValidator should raise ValueError for a dangling symlink.
    """
    target = tmp_path / "nonexistent"
    link = tmp_path / "dangling"
    link.symlink_to(target)
    with pytest.raises(ValueError) as excinfo:
        DirectoryValidator(link)
    assert f"Not a directory: {link}" in str(excinfo.value)
    """
    DirectoryValidator should raise ValueError when given a file path.
    """
    # Create a temporary file
    file_path = tmp_path / "a_file.txt"
    file_path.write_text("dummy content")
    with pytest.raises(ValueError) as excinfo:
        DirectoryValidator(file_path)
    assert f"Not a directory: {file_path}" in str(excinfo.value)
