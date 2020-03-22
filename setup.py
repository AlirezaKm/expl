from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='expl',
    version='1.0.1',
    packages=find_packages(exclude=['.venv', '.idea', 'build', 'dist', 'expl.egg-info']),
    url='https://github.com/AlirezaKm/expl',
    license='GPLv3',
    author='Alireza Km',
    author_email='alitm28@gmail.com',
    description='Generate exploit template',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['exploit', 'template', 'generator'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'expl=run:app'
        ]
    },
    install_requires=[
        'click',
        'Jinja2',
        'MarkupSafe'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
