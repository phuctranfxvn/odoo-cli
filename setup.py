from setuptools import setup, find_packages

setup(
    name="odoo-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "odoo=odoo_cli.cli:cli",
        ]
    },
    python_requires=">=3.6",
    author="Phúc",
    description="CLI tool to run Odoo projects using pew virtualenvs",
)
