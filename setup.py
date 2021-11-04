from distutils.core import setup
from setuptools import find_packages

setup(
    name="python-flask",
    version="0.0.1",
    description="API with Python and Flask",
    author="Marco Gattello",
    author_email="mgattello@gmail.com",
    url="https://github.com/mgattello/python-flusk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages= find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "aniso8601>=9.0.1",
        "attrs>=21.2.0",
        "click>=8.0.3",
        "Flask>=2.0.2",
        "Flask-RESTful>=0.3.9",
        "iniconfig>=1.1.1",
        "itsdangerous>=2.0.1",
        "Jinja2>=3.0.2",
        "MarkupSafe>=2.0.1",
        "packaging>=21.2",
        "pluggy>=1.0.0",
        "py>=1.10.0",
        "pyparsing>=2.4.7",
        "pytest>=6.2.5",
        "pytz>=2021.3",
        "six>=1.16.0",
        "toml>=0.10.2",
        "Werkzeug>=2.0.2"
    ]
)