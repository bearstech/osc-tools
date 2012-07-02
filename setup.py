#!/usr/bin/env python

from setuptools import setup

# http://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(name='osc-tools',
    version='0.0.1',
    package_dir={'': 'src'},
    url='http://github.com/bearstech/osc-tools',
    description="",
    long_description="""
""",
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Topic :: Artistic Software',
          'Topic :: Communications',
          'Topic :: Other/Nonlisted Topic',
          'Topic :: Scientific/Engineering :: Human Machine Interfaces',
          'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Networking',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        ],
    license="GPLv3",
    author="Mathieu Lecarme",
    packages=['osc-tools'],
    keywords=["osc"],
    scripts=['bin/'],
    zip_safe=True,
    install_requires=["pyOSC"],
)
