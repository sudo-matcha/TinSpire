import os
from shutil import make_archive
from sys import platform

run_dir = os.path.dirname(__file__)
os.path.abspath(run_dir)
parent_dir = (os.path.abspath(run_dir).split("\\") if platform == "win32" else os.path.abspath(run_dir).split("/"))[-1]
if parent_dir != "TinSpire":
    print("Please run this script in the root of the git directory")
    exit(1)

make_archive("PyLib", "zip", os.path.abspath("./src/tns"))