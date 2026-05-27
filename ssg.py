import argparse

parser = argparse.ArgumentParser()
parser.add_argument("action", help="Action you would like to perform. Supported actions: build.")
args = parser.parse_args()

print(args.action)