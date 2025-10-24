from setuptools import setup, find_packages

setup(
    name="GARP",
    version="1.0.0",
    author="KcanCurly",
    description="Send GARP with intervals",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/garp",
    packages=find_packages(),
    install_requires=[
        "scapy",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "garp.py=src.main:main",  
        ],
    },
)