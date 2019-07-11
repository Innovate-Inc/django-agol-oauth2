import os

from setuptools import find_packages, setup
#
# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()
#
# # allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="django-agol-oauth2",
    version="0.0.1",
    author="Travis Bock",
    author_email="tbock@innovateteam.com",
    license="MIT",
    description="Provide oauth2 agol login functionality to django projects",
    url="https://github.com/Innovate-Inc/django-agol-oauth2",
    packages=['agol_auth'],
    install_requires=['django-localflavor'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    include_package_data=True

)
