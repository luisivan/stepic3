#!/usr/bin/env python

from distutils.core import setup
import os

if os.environ.get('RELEASE') == '1':
    import stepic
    version = stepic.__version__
else:
    version = 'git'

setup(name='stepic3',
      version=version,
      description='Python image steganography, for Python 3',
      author='Lenny Domnitser',
      author_email='lenny@domnit.org',
      url='http://domnit.org/stepic/doc/',
      license='GPL',
      py_modules=['stepic'],
      scripts=['stepic'],
      data_files=[('share/doc/stepic', ['COPYING', 'TODO']),
                  ('share/man/man1', ['stepic.1'])],
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Environment :: Console',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Utilities',
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
          ]
      )
