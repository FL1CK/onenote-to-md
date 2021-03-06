import re
from setuptools import setup, find_packages

# import
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

version = "0.0.2"

setup(
    name='onenote-to-md',
    version=version,
    author='Samuel Flickinger',
    author_email='samuelflickinger@yahoo.com',
    license='MIT',
    description='A OneNote to Markdown (MD) converter with utility to automatically generate repo documentation from '
                'notes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/FL1CK/onenote-to-md',
    py_modules=['main', 'onenote_to_md'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        onenote-to-md=main:main
    """
)
