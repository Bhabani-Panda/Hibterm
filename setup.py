from setuptools import setup, find_packages

setup(
    name='HibTerm',
    version='1.0.0',
    author = 'Bhabani Shankar Panda',
    author_email = 'bhabani.panda1403@gmail.com',
    description = 'HibTerm is a CLI tool for fetching notices from IIIT Bhubaneswar\'s official portal - M-UMS',
    packages = find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'hibterm = hibterm.cli:test',
        ],
    },
)