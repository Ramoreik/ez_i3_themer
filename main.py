from src.themer import Themer
import argparse

def handle_args():
    parser = argparse.ArgumentParser(description='EZThemer made by Ramoreik')
    parser.add_argument('-t','--theme', type=str, help='Load Appearance theme from yaml file', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = handle_args()
    themer = Themer(args.theme)
    themer.execute()