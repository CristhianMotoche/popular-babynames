try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A project to get the popular babynames',
    'author': 'Cristhian Motoche',
    'url': 'github.com/CristhianMotoche/popular-babyname',
    'download_url': 'github.com/CristhianMotoche/popular-babyname',
    'author_email': 'cristhian.motoche@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['popular-babynames'],
    'scripts': [],
    'name': 'Popular Babynames'
}

setup(**config)
