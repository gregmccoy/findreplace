# findreplace
Quick find and replace script for replace items in code or plain text

```
usage: findreplace [-h] [--ignore IGNORE] [--text] old new folder

positional arguments:
  old              String to find
  new              String to replace old with
  folder           Location to recursively search in

optional arguments:
  -h, --help       show this help message and exit
  --ignore IGNORE  Regex for what the character before and after the replace
                   can be
  --text           Regex to match plain text outside of cod
```
