"""
Unit tests for scanner classes in synthetic_data_factory/tools/scanners.py
"""
import os
import pytest
from pathlib import Path

from test_data.synthetic_data.synthetic_data_factory.tools.explorer.explorer import DirectoryExplorer
from test_data.synthetic_data.synthetic_data_factory.tools.scanners.scanners import (
    TopLevelScanner,
    SubfolderMappingScanner,
    NestedSubfolderScanner,
    FileListingScanner
)


def setup_explorer(tmp_path: Path) -> DirectoryExplorer:
    """
    Creates a sample directory structure and returns a DirectoryExplorer.
 
    Structure:
      tmp_path/
        alpha/
          suba/
          subb/
        beta/
          subx/
            file1.txt
            __init__.py
          suby/
            nested/
              deepest/
        emptydir/
        rootfile.txt
        __pycache__/
        tools/
    """
    # Top-level folders
    alpha = tmp_path / "alpha"
    alpha.mkdir()
    (alpha / "suba").mkdir()
    (alpha / "subb").mkdir()

    beta = tmp_path / "beta"
    beta.mkdir()
    subx = beta / "subx"
    subx.mkdir()
    (subx / "file1.txt").write_text("data")
    (subx / "__init__.py").write_text("")

    suby = beta / "suby"
    suby.mkdir()
    nested = suby / "nested"
    nested.mkdir()
    (nested / "deepest").mkdir()

    # Empty directory
    (tmp_path / "emptydir").mkdir()

    # Root file
    (tmp_path / "rootfile.txt").write_text("root")

    # Excluded directories
    (tmp_path / "__pycache__").mkdir()
    (tmp_path / "tools").mkdir()

    return DirectoryExplorer(tmp_path, exclude=["__pycache__", "tools"])


def test_top_level_scanner(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = TopLevelScanner(explorer)
    result = scanner.scan()
    assert isinstance(result, list)
    assert set(result) == {"alpha", "beta", "emptydir"}


def test_top_level_scanner_empty(tmp_path: Path):
    # Only excluded dirs and files in root
    root = tmp_path
    (root / "__pycache__").mkdir()
    (root / "tools").mkdir()
    (root / "file.txt").write_text("x")
    explorer = DirectoryExplorer(root)
    scanner = TopLevelScanner(explorer)
    assert scanner.scan() == []


@pytest.mark.parametrize(
    "exclude_list,expected",
    [
        (['__pycache__', 'tools', 'alpha'], ['beta', 'emptydir']),
        (['__pycache__', 'tools', 'beta', 'emptydir'], ['alpha']),
    ],
)
def test_top_level_custom_exclude(tmp_path: Path, exclude_list, expected):
    explorer = setup_explorer(tmp_path)
    explorer_custom = DirectoryExplorer(tmp_path, exclude=exclude_list)
    scanner = TopLevelScanner(explorer_custom)
    assert sorted(scanner.scan()) == sorted(expected)


def test_subfolder_mapping_scanner(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = SubfolderMappingScanner(explorer)
    mapping = scanner.scan()
    assert set(mapping.keys()) == {"alpha", "beta", "emptydir"}
    assert sorted(mapping['alpha']) == ["suba", "subb"]
    assert sorted(mapping['beta']) == ["subx", "suby"]
    assert mapping['emptydir'] == []


def test_nested_subfolder_scanner(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = NestedSubfolderScanner(explorer)
    nested = scanner.scan()
    assert nested['alpha']['suba'] == []
    assert nested['alpha']['subb'] == []
    assert nested['beta']['subx'] == []
    assert nested['beta']['suby'] == ['nested']


def test_nested_subfolder_ignores_deeper(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = NestedSubfolderScanner(explorer)
    nested = scanner.scan()
    # 'deepest' should not appear under beta->suby
    assert 'deepest' not in nested['beta']['suby']


def test_file_listing_scanner(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = FileListingScanner(explorer)
    files_map = scanner.scan()
    assert files_map['alpha']['suba'] == []
    assert files_map['alpha']['subb'] == []
    assert files_map['beta']['subx'] == ['file1.txt']
    assert files_map['beta']['suby'] == []
    assert files_map['emptydir'] == {}


def test_file_listing_excludes_init(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    scanner = FileListingScanner(explorer)
    files_map = scanner.scan()
    assert '__init__.py' not in files_map['beta']['subx']


def test_file_listing_ignores_directories(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    suby = tmp_path / 'beta' / 'suby'
    (suby / 'somefile.txt').write_text('x')
    (suby / 'adir').mkdir()
    scanner = FileListingScanner(explorer)
    files = scanner.scan()['beta']['suby']
    assert files == ['somefile.txt']


@pytest.mark.skipif(not hasattr(os, 'symlink'), reason="Symlinks unsupported")
def test_symlink_as_top_level(tmp_path: Path):
    explorer = setup_explorer(tmp_path)
    real = tmp_path / 'gamma'
    real.mkdir()
    link = tmp_path / 'delta'
    link.symlink_to(real)
    result = TopLevelScanner(explorer).scan()
    assert 'delta' in result


@pytest.mark.parametrize(
    "scanner_cls",
    [TopLevelScanner, SubfolderMappingScanner, NestedSubfolderScanner, FileListingScanner],
)
def test_scanners_are_idempotent(tmp_path: Path, scanner_cls):
    explorer = setup_explorer(tmp_path)
    scanner = scanner_cls(explorer)
    first = scanner.scan()
    second = scanner.scan()
    assert first == second
