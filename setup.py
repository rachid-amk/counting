try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'counting random number a, b, and c',
    'author': 'rachid_amk',
    'url': '',
    'download_url': '',
    'author_email': 'rachid.drid@gmail.com',
    'version': 'v0.1',
    'install_requires': [],
    'packages': ['counting'],
    'script': [],
    'name': 'counting'
    }

setup(**config)
