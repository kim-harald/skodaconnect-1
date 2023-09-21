from setuptools import setup, find_packages

# read the contents of your README file
from os import path
from skodaconnect.__version__ import __version__ as lib_version
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def local_scheme(version):
    return ""

setup(
    name='skodaconnect',
    version=lib_version,
    description='Communicate with Skoda Connect',
    author='lendy007',
    author_email='lendik@gmail.com',
    url='https://github.com/skodaconnect/skodaconnect',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    provides=["skodaconnect"],
    install_requires=[
        "aiohttp",
        "beautifulsoup4",
        "cryptography",
        "lxml", 
        "pyjwt"
    ],
    #use_scm_version=True,
    use_scm_version={"local_scheme": local_scheme},
    setup_requires=[
        'setuptools_scm', "wheel"
    ]
)
