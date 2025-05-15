from setuptools import setup, find_packages

setup(
    name="finderplusplus",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "spacy",
        "rapidfuzz"
    ],
    entry_points={
        "console_scripts": [
            "fpp=cli:main"
        ]
    },
)