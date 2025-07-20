import tomllib
import os
import urllib
import zipfile
import subprocess

from typing import List

# build_path function
def build_path(PATH : List) -> str:
    return os.path.abspath(os.path.join(*PATH))

# Current File Path
FILE_PATH = os.getcwd()
DATA_TOML_FN = build_path([FILE_PATH, "url_data.toml"])
BASH_SCRIPT = build_path([FILE_PATH, "get_and_extract_zip.sh"])
ROW_DATA_FP = build_path([FILE_PATH, "data"])

## Define files path
with open(DATA_TOML_FN, "rb") as f:
    data_url = tomllib.load(f)

for clasification_system, concordance_url in data_url.items():
    ## Directory where the file will be saved
    CLASIFICATION_SYSTEM_DIR = build_path([ROW_DATA_FP, clasification_system.lower().replace(" ", "_").replace("1988/", "")])

    ## If the directory is not present, create it
    if not os.path.exists(CLASIFICATION_SYSTEM_DIR):
        os.mkdir(CLASIFICATION_SYSTEM_DIR)

    for concordance, url in concordance_url.items():

        subprocess.run([f"{BASH_SCRIPT} {CLASIFICATION_SYSTEM_DIR} {url}"], shell = True)
