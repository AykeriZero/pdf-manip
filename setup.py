"""
Command Line Tool for Rotating PDFs

github: AykeriZero

Alex Song <songya@umich.edu>
"""

from setuptools import setup

setup(
    name='pdfmanip',
    version='0.1.0',
    packages=['pdfmanip'],
    include_package_data=True,
    install_requires=[
        'click==7.0',
        'pypdf2==1.26.0',
        'pycodestyle==2.4.0',
        'pydocstyle==3.0.0',
        'pylint==2.2.2',
        'pytest==4.1.0',
    ],
    entry_points={
        'console_scripts': [
            'pdfmanip = pdfmanip.__main__:main'
        ]
    },
)
