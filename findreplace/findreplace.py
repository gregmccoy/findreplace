#!/usr/bin/env python3

import re
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("old", help="String to find")
parser.add_argument("new", help="String to replace old with")
parser.add_argument("folder", help="Location to recursively search in")
parser.add_argument("--ignore", dest='ignore', help="Regex for what the character before and after the replace can be")
parser.add_argument("--text", action='store_true', dest='text', help="Regex to match plain text outside of code")
args = parser.parse_args()

def main(args):
    ignore = "[^-_=+/\"'a-z]"
    if args.ignore:
        ignore = args.ignore
    oldstr = args.old
    newstr = args.new
    if not args.text:
        regex = "[^a-z]" + oldstr + "[^a-z]"
    else:
        regex = ignore + oldstr + "({}|[s])".format(ignore)

    for dirpath, dirnames, filenames in os.walk(args.folder):
        for fname in filenames:
            fullname = os.path.join(dirpath, fname)
            if "/.git/" not in dirpath and not os.path.islink(fullname):
                file_match(fullname, regex, oldstr, newstr)
    print(regex)
    re.search(regex, "")


def file_match(fname, pattern, old, new):
    date = ""
    newdata = []
    found = False
    try:
        with open(fname, "rt", errors='ignore') as f:
            data = f.readlines()
    except Exception as e:
        print("Error opening file\n {}".format(e))
        return -1

    for i, line in enumerate(data):
        match = re.search(pattern, line)
        if match:
            found = True
            print("%s: %i: %s" % (fname, i+1, match.group(0)))
            replacestr = match.group(0).replace(old, new)
            line = line.replace(match.group(0), replacestr)
        newdata.append(line)
    if found:
        with open(fname, "w") as f:
            for line in newdata:
                f.write(line)
main(args)
