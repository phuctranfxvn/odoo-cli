from setuptools import setup, find_packages
version = {}
with open("odoorunner/__version__.py") as f:
    exec(f.read(), version)

setup(
    name="odoorunner",
    version=version["__version__"],
    author="Phuc (Tran Thanh)",
    author_email='phuctran.fx.vn@gmail.com',
    description="Runner tool to run Odoo project using pew virtualenvs",
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phuctranfxvn/odoorunner',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "odoorunner=odoorunner.runner:runner",
        ]
    },
    python_requires=">=3.6",

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
