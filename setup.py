from setuptools import setup, find_packages

setup(
    name="PyCt6",
    version="6.0.3",    
    author="D. Liam Mc.",
    author_email="dliammc@duck.com",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    description="A modern and customizable python GUI interface library built from the PySide6 library",
    url="https://github.com/Dliammc/CustomPyQt/",
    license="MIT License",
    packages=find_packages(),
    install_requires=[
        "PySide6",
        "typing",
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