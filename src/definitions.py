import os
from getpass import getuser


HOME_FOLDER = os.path.join(os.path.sep, "home", getuser())
CURRENT_FOLDER = os.path.dirname(__file__)
TEMPLATES_FOLDER = os.path.join(CURRENT_FOLDER, "templates")
BACKUP_FOLDER = os.path.join(HOME_FOLDER, ".themer")

WILDCARDS = {
    "~" : HOME_FOLDER,
    "./" : CURRENT_FOLDER + "/"
}

EXECUTABLE_EXTENSIONS = [
    "sh",
    "py",
    "ksh"
]

