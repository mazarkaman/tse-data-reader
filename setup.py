import pathlib
from setuptools import find_packages,setup

PATH = pathlib.Path(__file__).parent

README = (PATH / "README.md").read_text()

setup(
    name="tse-data-reader",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="office@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        'pandas>=0.25.3,<0.26.0',
        'requests>=2.22.0,<2.23.0'
        'jdatetime>=3.6.2,<3.7.0'
        'beautifulsoup4>=4.8.1,<4.9.0'
    ],
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    }
)