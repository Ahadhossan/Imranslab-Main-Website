"""
tests/tools/test_explorer.py

Unit tests for DirectoryExplorer in synthetic_data_factory/tools/explorer.py
"""

import os
import pytest
from pathlib import Path

from test_data.synthetic_data.synthetic_data_factory.tools.explorer.explorer import DirectoryExplorer


def create_structure(tmp_path: Path):
    """
    Create a sample structure:
      tmp_path/
        dir1/
          sub1/
          sub2/
        dir2/
        __pycache__/
        tools/
        file.txt
    """
    # Directories
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "sub1").mkdir()
    (tmp_path / "dir1" / "sub2").mkdir()
    (tmp_path / "dir2").mkdir()
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "tools").mkdir()
    # Files
    (tmp_path / "file.txt").write_text("hello")
    (tmp_path / "dir2" / "inner.txt").write_text("inner")
    return tmp_path


def test_list_subdirs_basic(tmp_path: Path):
    """
    list_subdirs() should return only immediate subdirectories,
    excluding default excluded names.
    """
    root = create_structure(tmp_path)
    explorer = DirectoryExplorer(root)
    subdirs = {p.name for p in explorer.list_subdirs()}
    assert subdirs == {"dir1", "dir2"}


def test_list_subdirs_custom_exclude(tmp_path: Path):
    """
    Passing an `exclude` list should filter out those names as well.
    """
    root = create_structure(tmp_path)
    # now also exclude 'dir2'
    explorer = DirectoryExplorer(root, exclude=['__pycache__', 'tools', 'dir2'])
    subdirs = {p.name for p in explorer.list_subdirs()}
    assert subdirs == {"dir1"}


def test_list_subdirs_nested(tmp_path: Path):
    """
    list_subdirs(path=some_subdir) should operate relative to that directory.
    """
    root = create_structure(tmp_path)
    explorer = DirectoryExplorer(root)
    dir1 = root / "dir1"
    subs = {p.name for p in explorer.list_subdirs(path=dir1)}
    assert subs == {"sub1", "sub2"}


def test_list_files_basic(tmp_path: Path):
    """
    list_files() should list only files, not directories.
    """
    root = create_structure(tmp_path)
    explorer = DirectoryExplorer(root)
    files = {p.name for p in explorer.list_files(path=root)}
    assert files == {"file.txt"}


def test_symlink_to_directory(tmp_path: Path):
    """
    A symlink pointing to a real directory should be listed by list_subdirs().
    """
    real = tmp_path / "real_dir"
    real.mkdir()
    link = tmp_path / "link_dir"
    link.symlink_to(real)
    explorer = DirectoryExplorer(tmp_path)
    subdirs = {p.name for p in explorer.list_subdirs()}
    assert "link_dir" in subdirs


@pytest.mark.skipif(not hasattr(os, 'symlink'), reason="OS does not support symlinks")
def test_symlink_to_excluded(tmp_path: Path):
    """
    Even if a symlink exists, if its name is in `exclude`, it should be skipped.
    """
    real = tmp_path / "real_dir"
    real.mkdir()
    link = tmp_path / "tools"
    # pretend 'tools' is a symlink to real_dir
    link.symlink_to(real)
    explorer = DirectoryExplorer(tmp_path)
    subdirs = {p.name for p in explorer.list_subdirs()}
    assert "tools" not in subdirs


def test_empty_directory(tmp_path: Path):
    """
    If the directory has no subdirectories (other than excluded),
    list_subdirs should return an empty list.
    """
    (tmp_path / "__pycache__").mkdir()
    explorer = DirectoryExplorer(tmp_path)
    subs = explorer.list_subdirs()
    assert subs == []


def test_list_files_empty(tmp_path: Path):
    """
    If there are no files, list_files should return an empty list.
    """
    folder = tmp_path / "empty_dir"
    folder.mkdir()
    explorer = DirectoryExplorer(tmp_path)
    # ensure it lists subdirs first
    subdirs = explorer.list_subdirs()
    # now test files inside empty_dir
    files = explorer.list_files(path=folder)
    assert files == []
