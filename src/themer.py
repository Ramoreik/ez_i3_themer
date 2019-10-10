import os
import yaml
import pprint
import traceback
from src.classes.software import Software
from getpass import getuser
from shutil import copyfile, rmtree
import tarfile
from jinja2 import Template


HOME_FOLDER = os.path.join(os.path.sep, "home", getuser())
CURRENT_FOLDER = os.path.dirname(__file__)
TEMPLATES_FOLDER = os.path.join(CURRENT_FOLDER, "templates")
BACKUP_TEMP_FOLDER = os.path.join(HOME_FOLDER, ".themer_tmp")
BACKUP_FOLDER = os.path.join(HOME_FOLDER, ".themer")


WILDCARDS = {
    "~" : HOME_FOLDER
}


class Themer():

    def __init__(self, config_file, **kwargs):
        self.softwares = []
        self.config_file = config_file
        self.configuration = self.load_theme()

    def instanciate_softwares(self):
        for software_config in self.configuration["softwares"]:
            software_config["templates"] = self.expand_template(software_config["templates"])
            software = Software(
                software_config["name"],
                software_config["templates"],
                software_config.get("refresh",[]),
                BACKUP_FOLDER
                )
            self.softwares.append(software)

    def expand_template(self, templates):
        expanded_templates = []
        for template in templates:
            template["src"] = os.path.join(TEMPLATES_FOLDER, template["src"])
            expanded_templates.append(template)
        return expanded_templates

    def execute(self):
        self.instanciate_softwares()
        self.create_backup_dir()
        for software in self.softwares:
            print("Configuring {} ...".format(software.name))
            software.execute()

    def load_theme(self):
        parsed_theme = self.expand_wilcards(self.config_file)
        return self.load_yaml(parsed_theme)

    def expand_wilcards(self, theme_file):
        theme_content = open(theme_file, 'r').read()
        for wildcard in WILDCARDS:
            if wildcard in theme_content:
                theme_content = theme_content.replace(wildcard, WILDCARDS[wildcard])
        return theme_content

    def load_yaml(self, theme_content):
        return yaml.safe_load(theme_content)

    def create_backup_dir(self):
        if not os.path.exists(BACKUP_TEMP_FOLDER):
            os.makedirs(BACKUP_TEMP_FOLDER)

    def __str__(self):
        pp = pprint.PrettyPrinter()
        return pp.pformat(self.configuration)
