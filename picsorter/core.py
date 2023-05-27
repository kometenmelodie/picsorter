import datetime
from pathlib import Path


def _get_creation_date(filename: Path) -> str:
    """Get time of most recent content modification (in seconds)
    on Windows system"""
    creation_date_seconds = filename.stat().st_mtime

    # convert to date string
    creation_date = datetime.datetime.fromtimestamp(
        creation_date_seconds
    ).strftime("%Y-%m-%d_%H-%M-%S")

    return creation_date


def _rename_file(
    filename: Path, append_old_name: bool = False, verbose: bool = True
) -> None:
    """Rename one file with its creation date."""
    creation_date = _get_creation_date(filename)

    if append_old_name:
        creation_date = f"{creation_date}_{filename.stem}"

    # replace stem with creation date
    new_file_name = filename.with_stem(creation_date)
    if verbose:
        print(new_file_name)

    # rename the file
    filename.rename(new_file_name)


def rename_multiple_files(folder: Path, file_extension: str = "jpg") -> None:
    """Rename all files that match the file_extension
    within the given folder."""
    # iterate over all files within the specific folder
    for file in list(folder.glob(f"*.{file_extension}")):
        file = Path(file)
        try:
            _rename_file(filename=file, append_old_name=False)
        except FileExistsError:
            # append old file name to prevent duplicates
            _rename_file(filename=file, append_old_name=True)
