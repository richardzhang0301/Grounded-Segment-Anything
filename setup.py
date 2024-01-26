from setuptools import setup, find_packages
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def load_requirements():
    requirements_file_name = "requirements.txt"
    requires = []
    with open(requirements_file_name) as f:
        for line in f:
            if line:
                requires.append(line.strip())
    return requires


VERSION = '0.0.1'
DESCRIPTION = 'Forked wrapped Ground Segment Anything'
LONG_DESCRIPTION = 'Forked wrapped Ground Segment Anything'

# Setting up
setup(
    name="grounded-segment-anything",
    version=VERSION,
    author="Richard Zhang",
    author_email="<richard.zh@linquet.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    ackages=find_packages(),
    install_requires=load_requirements(),
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)