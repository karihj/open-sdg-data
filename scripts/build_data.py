"""
Created on Sun May 13 2018

@author: dashton

This is the parent script for building the data outputs. It loads the
raw data from csv and sends it through the various processors to
output the main data, edges, and headline in csv and json format.

"""

import os
import yamlmd

from sdg.build import build_data

if __name__ == '__main__':
    # Error checking (extremely rudimentary)
    for root, dirs, files in os.walk("."):
        for name in files:
            try:
                if name.endswith(".md"):
                    data = yamlmd.read_yamlmd(os.path.join(root, name))
            except Exception as e:
                print("Error in " + str(os.path.join(root, name)))
                print("Error is " + str(e))
    status = build_data()
    if(not status):
        raise RuntimeError("Failed data build")
    else:
        print("Success")
