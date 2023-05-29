from distutils.dir_util import copy_tree, remove_tree
from pathlib import Path

import pytest

from picsorter.core import (
    _get_creation_date,
    _rename_file,
    rename_multiple_files,
)


def copy_directory(new_directory_name: str = "tests/pictures_copy"):
    """Copy directory with pictures to perform tests."""
    copy_tree("tests/pictures", new_directory_name)


def delete_directory(directory_name: str = "tests/pictures_copy"):
    """Delete a directory and its content."""
    remove_tree(directory_name)


@pytest.mark.parametrize(
    "picture_path, expected",
    [
        (Path("tests/pictures/bird.jpg"), "2023-05-29_08-07-04"),
        (Path("tests/pictures/ladybug.jpg"), "2023-05-29_07-52-22"),
    ],
)
def test_get_creation_date(picture_path, expected):
    assert expected == _get_creation_date(picture_path)


@pytest.mark.parametrize(
    "picture_path, expected, expected_append_old_name",
    [
        (
            Path("tests/pictures_copy/bird.jpg"),
            "2023-05-29_08-07-04.jpg",
            "2023-05-29_08-07-04_bird.jpg",
        ),
        (
            Path("tests/pictures_copy/ladybug.jpg"),
            "2023-05-29_07-52-22.jpg",
            "2023-05-29_07-52-22_ladybug.jpg",
        ),
    ],
)
def test_rename_file(picture_path, expected, expected_append_old_name):
    """Test renaming files to creation date and to creation date with old
    file name appended."""
    new_path = "tests/pictures_copy"
    # first copy directory 'pictures' with its content
    copy_directory(new_directory_name=new_path)

    # rename file
    _rename_file(picture_path)
    # check if file with new name exists
    assert (Path(new_path) / expected).exists()

    # delete directory
    delete_directory(directory_name=new_path)

    # again, copy directory
    copy_directory(new_directory_name=new_path)
    # rename file and append original file name
    _rename_file(picture_path, append_old_name=True)
    assert (Path(new_path) / expected_append_old_name).exists()
    delete_directory(directory_name=new_path)


def test_rename_multiple_files():
    new_path = "tests/pictures_copy"
    copy_directory(new_directory_name=new_path)

    rename_multiple_files(Path(new_path), file_extension="jpg")

    for renamed_file in ["2023-05-29_08-07-04.jpg", "2023-05-29_07-52-22.jpg"]:
        assert (Path(new_path) / renamed_file).exists()

    # ladybug.jpg in pictures_copy/more_pictures should have kept its name
    assert (Path(new_path) / "more_pictures/ladybug.jpg").exists()
    delete_directory(directory_name=new_path)
