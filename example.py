from pathlib import Path

from picsorter import rename_multiple_files

# rename both jpg-files in tests/pictures
p = Path("tests/pictures")

rename_multiple_files(p, file_extension="jpg")
