from pathlib import Path
import os
import pkg_resources
import json

file_name="config.json"
folder_name="zoomstarter_config"
default_config = pkg_resources.resource_filename("zoom","data/"+file_name)
home = str(Path.home())

def get_config(number):
    if number==1:
        return default_config 
    return create_config() 

def create_config():
    if os.path.isdir(folder_name)==False:
        os.makedirs(folder_name)
        os.chdir(folder_name)
        with open(file_name, 'w') as f:
            json.dump({}, f)
    return format_location()

def format_location():
    location=home+ "/"+ folder_name+"/"+file_name
    return location