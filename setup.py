from setuptools import setup, find_packages

setup(
    name="explorateur_cli",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "explorateur=main:main"
        ]
    },
)
