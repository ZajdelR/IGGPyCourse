
# point.py

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--coordinates", nargs=2)

args = parser.parse_args()

print(args)
