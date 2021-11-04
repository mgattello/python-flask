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
)
