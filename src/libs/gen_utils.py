import os
import stat
import yaml
from datetime import datetime
from getpass import getuser

HOME_FOLDER = os.path.join(os.path.sep, "home", getuser())
WILDCARDS = {
    "~" : HOME_FOLDER
}
EXECUTABLE_EXTENSIONS = [
    "sh",
    "py",
    "ksh"
]


def expand_wilcards(theme_file):
    theme_content = open(theme_file, 'r').read()
    for wildcard in WILDCARDS:
        if wildcard in theme_content:
            theme_content = theme_content.replace(wildcard, WILDCARDS[wildcard])
    return theme_content


def load_yaml(theme_content):
    return yaml.safe_load(theme_content)


def create_backup_dir(location):
    if not os.path.exists(location):
        os.makedirs(location)


def timestamp():
    return str(datetime.timestamp(datetime.now()))


def adjust_mode(dest):
    file_extension = os.path.basename(dest).split('.')[-1]
    if file_extension in EXECUTABLE_EXTENSIONS:
        current_mode = os.stat(dest).st_mode
        os.chmod(dest, current_mode | stat.S_IEXEC)

