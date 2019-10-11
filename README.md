# I3WM EZ Themer

## What is it ?

It is a themer that uses jinja2 templates to configure a variety of programs.

It could be modified to include pretty much every program that has configuration files as long as we take the time to make adequate templates. 

### Installation :

Simply clone the repo and run the appropriate installation script from the scripts folder.

```bash
git clone https://github.com/Ramoreik/ez_i3_themer.git
cd ez_i3_themer/scripts
# Run the install script for your distribution
bash install_arch.sh
# Install requirements
pip install -r requirements.txt
```

Once that's done you can either use one of my themes and change the wallpaper(as it is not in the repo), or you can craft your own from scratch.

Once you have your theme you can run the following command : 

```
python main.py -t themes/YOUR_THEME.yml
```

Enjoy !

### How does it work?

It uses a configuraton files with a list of different softwares to configure, every software can have multiple template files. Every software can also have a refresh method to update the appearance as the program executes.

#### Templates :

Every software has a list of templates with a source, destination and configuration tag. 

The source should be within the templates folder, destination is wherever you want on your computer and the configuration tag contains all the variables to be replaced in the template.

#### Refresh :

Basically, the refresh tag takes a list and directly passes it through to your shell using subprocess.call.

#### Example of the configuration for a software :

```yaml
  - name: nitrogen
    refresh:
      - nitrogen
      - "--set-zoom-fill"
      - "~/Pictures/wallpapers/1569438865684.jpg"
    templates:
      - src: nitrogen/nitrogen.j2
        dest: ~/.config/nitrogen/bg-saved.cfg
        config:
          wallpaper: ~/Pictures/wallpapers/1569438865684.jpg
```

The bash install scripts were taken and modified for my purpose from : https://github.com/unix121/i3wm-themer
Most of the art for the default wallpapers came from this wonderful artist ! : https://www.artstation.com/aenamiart
