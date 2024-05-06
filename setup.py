from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='SQLconn',
    version='0.0.2',
    description='This package facilitates easy SQL database integration.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='janyoungjin',
    install_requires=['mysqlclient', 'pandas', 'cx_oracle', 'psycopg2', 'pymssql'],
    packages=find_packages(exclude=[]),
    url='https://github.com/janyoungjin/SQLConn',
    keywords=['mysql', 'postgresql', 'sqlite', 'mssql', 'oracle', 'sql']
)
