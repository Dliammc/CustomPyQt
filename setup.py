from setuptools import setup, find_packages

setup(
    name="PyCt",
    version="0.0.3",    
    author="D. Liam Mc.",
    author_email="dliammc@duck.com",
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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="<3.14, >=3.9",

    project_urls={                   
        "Source": "https://github.com/Dliammc/CustomPyQt",
    },
    
)