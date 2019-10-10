import os
import yaml
import pprint
import traceback
import src.libs.gen_utils as gen_utils
from src.classes.software import Software
from getpass import getuser
from jinja2 import Template


HOME_FOLDER = os.path.join(os.path.sep, "home", getuser())
CURRENT_FOLDER = os.path.dirname(__file__)
TEMPLATES_FOLDER = os.path.join(CURRENT_FOLDER, "templates")
BACKUP_TEMP_FOLDER = os.path.join(HOME_FOLDER, ".themer_tmp")
BACKUP_FOLDER = os.path.join(HOME_FOLDER, ".themer")


class Themer():

    def __init__(self, config_file, **kwargs):
        self.softwares = []
        self.config_file = config_file
        self.configuration = self.parse_theme()

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
        gen_utils.create_backup_dir(BACKUP_FOLDER)
        for software in self.softwares:
            print("Configuring {} ...".format(software.name))
            software.configure()

    def parse_theme(self):
        parsed_theme = gen_utils.expand_wilcards(self.config_file)
        return gen_utils.load_yaml(parsed_theme)

    def __str__(self):
        pp = pprint.PrettyPrinter()
        return pp.pformat(self.configuration)
