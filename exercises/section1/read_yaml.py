#!/usr/bin/env python
from __future__ import print_function
import yaml
from pprint import pprint

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

if __name__ == "__main__":
    # filename = "sect1_ex2.yml"
    filename = raw_input("Enter filename: ")
    pprint(read_yaml(filename))
