from setuptools import setup
import re,os
from setuptools import find_packages
from pip._internal.req import parse_requirements

install_reqs = [str(req.requirement) for req in parse_requirements('requirements.txt', session='hack')]

def find():
    print(find_packages())
    return find_packages()

setup(
    name='zoomstarter',
    version='1.0',
    packages=["zoom","zoom.classes","zoom.gui","zoom.classes.impl","zoom.util"],
    package_data={'': ['data/config.json']},
    include_package_data=True,
    url='https://github.com/viktorcvetanovic',
    author='vikitor',
    author_email='viktorcvetanovic@gmail.com',
    description='Zoom app starter',
    install_requires=install_reqs,
    entry_points={
        "console_scripts": ["zoomstarter=zoom.main:main","zoomstartergui=zoom.main_gui:main"]

    }
)
