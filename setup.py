import requests
from setuptools import setup, find_packages

def fetch_readme(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

# URL of the README file
readme_url = 'https://raw.githubusercontent.com/Dliammc/CustomPyQt/refs/heads/main/README.md'

setup(
    name="PyCt6",
    version="6.1.0",    
    author="D. Liam Mc.",
    author_email="dliammc@duck.com",
    long_description=fetch_readme(readme_url),
    long_description_content_type='text/markdown',
    description="A modern and customizable python GUI interface library built from the PySide6 library",
    url="https://github.com/Dliammc/CustomPyQt/",
    license="MIT License",
    packages=find_packages(),
    install_requires=[
        "PySide6",
    ],
    include_package_data=True,

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="<3.14, >=3.9",

    project_urls={                   
        "Source": "https://github.com/Dliammc/CustomPyQt",
    },

)
