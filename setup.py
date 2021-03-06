
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='servicectl',
    version='0.0.0',
    description='Docker stack deployment manager',
    python_requires='==3.*,>=3.6.0',
    project_urls={"repository": "https://github.com/TheEdgeOfRage/servicectl"},
    author='Pavle Portic',
    author_email='pavle.portic@tilda.center',
    license='BSD-3-Clause',
    keywords='docker service deployment',
    packages=['servicectl'],
    package_dir={"": "."},
    package_data={},
    install_requires=['docker==4.*,>=4.1.0'],
)
