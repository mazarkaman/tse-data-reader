import pathlib
from setuptools import find_packages, setup

PATH = pathlib.Path(__file__).parent

README = (PATH / "README.md").read_text()

setup(
    name="tse-data-reader",
    version="0.1.0",
    description="reads data from tsetmc.com website",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mazarkaman/tse-data-reader.git",
    author="M.Azarkaman",
    author_email="Azarkaman.net@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        'pandas>=0.25.3,<0.26.0',
        'requests>=2.22.0,<2.23.0',
        'jdatetime>=3.6.2,<3.7.0',
        'beautifulsoup4>=4.8.1,<4.9.0'
    ],
    project_urls={
        "Source Code": "https://github.com/mazarkaman/tse-data-reader.git",
    }
)
