import os
import pprint
from jinja2 import Template
from datetime import datetime
from shutil import copyfile
from subprocess import call


class Software():
    def __init__(self, name, templates, refresh, backup_dir):
        self.name = name
        self.templates = templates
        self.refresh = refresh
        self.backup_dir = os.path.join(backup_dir, self.name, self.timestamp())

    def execute(self):
        self.validate_templates_integrity()
        self.backup()
        self.render_templates()
        self.refresh_software()

    def render_templates(self):
        for template in self.templates:
            prep_template = Template(open(template["src"], 'r').read())
            rendered_template = prep_template.render(template["config"])
            open(template["dest"], 'w').write(rendered_template)

    def refresh_software(self):
        if self.refresh != []:
            f = open(os.devnull,'w')
            call(self.refresh, stdout=f, stderr=f)
        else:
            print("\t{} >> no refresh method was specified".format(self.name))

    def timestamp(self):
        return str(datetime.timestamp(datetime.now()))

    def validate_templates_integrity(self):
        for template in self.templates:
            if  "src" not in template \
                    or "dest" not in template \
                    or "config" not in template:
                print("{} >> one of the template is lacking a necessary \
                        element please configure correctly".format(self.name))
                exit(1)

    def create_backup_dir(self):
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup(self):
        self.create_backup_dir()
        for template in self.templates:
            destination = os.path.join(self.backup_dir, os.path.basename(template["dest"]))
            if os.path.exists(template["dest"]):
                copyfile(template["dest"], destination)


