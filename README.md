# picsorter 🐍

... is a small Python tool to rename pictures to their creation dates.

## Installation

In order to install the project, `python = "^3.11"` is necessary. To set up
your environment simply type

```shell
poetry install
```

which will install all dependencies. 

## Usage

For example, to rename both `.jpg`-files in the `tests/pictures` directory, 
create a new `.py` script with following content.

````python
from pathlib import Path

from picsorter import rename_multiple_files

p = Path("tests/pictures")

# rename both jpg-files in tests/pictures
rename_multiple_files(p, file_extension="jpg")
````

`picsorter` renames only files which match the given `file_extension`.
