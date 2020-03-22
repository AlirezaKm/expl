from setuptools import setup, find_packages

setup(
    name='expl',
    version='1.0.0',
    packages=find_packages(exclude=['.venv', '.idea', 'build', 'dist', 'expl.egg-info']),
    url='',
    license='GPLv3',
    author='Alireza Km',
    author_email='alitm28@gmail.com',
    description='Generate exploit template',
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
    ]
)
