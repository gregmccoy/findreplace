# findreplace
Replace only plain text within HTML by checking the character before and after the search term

```
usage: findreplace.py [-h] [--ignore IGNORE] old new folder

positional arguments:
  old              String to find
  new              String to replace old with
  folder           Location to recursively search in

optional arguments:
  -h, --help       show this help message and exit
  --ignore IGNORE  Regex for what the character before and after the replace
                   can be
```
