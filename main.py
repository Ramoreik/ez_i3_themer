from src.classes.themer import Themer
import argparse

# TODO: Remake install scripts to be more adequate and modern, also to include more technologies for arch and ubuntu
# TODO: Add templates with an additionnal layer of abstraction, like main color, accents, etc. 
        # The goal is to make customization very simple for everynone

def handle_args():
    parser = argparse.ArgumentParser(description='EZThemer made by Ramoreik')
    parser.add_argument('-t','--theme', type=str, help='Load Appearance theme from yaml file', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = handle_args()
    themer = Themer(args.theme)
    themer.execute()