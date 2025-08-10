#!/usr/bin/env python3
"""
Setup configuration for Ultron Website Analyzer
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="ultron-analyzer",  # Change this if name is taken
    version="1.2",
    author="Om Pandey",  # Replace with your name
    author_email="iamompandey.it@gmail.com",  # Replace with your email
    description="🤖 Advanced website performance analyzer and optimizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ompandey07/Ultron",  # Replace with your repo
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "excel": ["openpyxl>=3.0.0"],
        "full": ["openpyxl>=3.0.0", "beautifulsoup4>=4.9.0"],
    },
    entry_points={
        "console_scripts": [
            "ultron=ultron.cli:main",
            "ultron-analyzer=ultron.cli:main",
        ],
    },
    keywords="website analyzer performance seo security optimization",
    project_urls={
        "Bug Reports": "https://github.com/ompandey07/Ultron/issues",
        "Source": "https://github.com/ompandey07/Ultron",
        "Documentation": "https://github.com/ompandey07/Ultron#readme",
    },
)