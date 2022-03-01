from pathlib import Path
import os
import pkg_resources
import json

file_name="config.json"
folder_name=".zoomstarter"
default_config = pkg_resources.resource_filename("zoom","data/"+file_name)
home = str(Path.home())

def get_config(number):
    if number==1:
        return default_config 
    return create_config() 

def create_config():
    directory=os.path.join(home,folder_name)
    if not os.path.isdir(directory):
        os.makedirs(directory)
        with open(os.path.join(directory,file_name), 'w') as f:
            json.dump({}, f)
    return format_location()

def format_location():
    location=os.path.join(home,folder_name,file_name)
    return location


def execute_command(command):
    os.system(command)
