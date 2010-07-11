import setuptools
import sys
import os

PTH_FILE = '''\
import pytest_cov_init; pytest_cov_init.init()
'''

UNKNOWN_SITE_PACKAGES_DIR ='''\
Failed to find site-packages or dist-packages dir to put pth file in.
Sub processes will not have coverage collected.

To measure sub processes put the following in a file called pytest_cov.pth:
'''

setuptools.setup(name='pytest-cov',
                 version='1.0a1',
                 description='py.test plugin for coverage reporting with support for both centralised and distributed testing',
                 long_description=open('README.txt').read().strip(),
                 author='Meme Dough',
                 author_email='memedough@gmail.com',
                 url='http://bitbucket.org/memedough/pytest-cov/overview',
                 py_modules=['pytest_cov',
                             'pytest_cov_init'],
                 install_requires=['py>=1.3.2',
                                   'pytest-xdist>=1.4',
                                   'coverage>=3.3.1'],
                 entry_points={'pytest11': ['pytest_cov = pytest_cov']},
                 license='MIT License',
                 zip_safe=False,
                 keywords='py.test pytest cover coverage distributed parallel',
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python',
                              'Programming Language :: Python :: 2.4',
                              'Programming Language :: Python :: 2.5',
                              'Programming Language :: Python :: 2.6',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3.0',
                              'Programming Language :: Python :: 3.1',
                              'Topic :: Software Development :: Testing'])

if sys.argv[1] in ('install', 'develop'):
    for path in sys.path:
        if 'site-packages' in path or 'dist-packages' in path:
            path = os.path.dirname(path)
            pth_file = open(os.path.join(path, 'pytest_cov.pth'), 'w')
            pth_file.write(PTH_FILE)
            pth_file.close()
            break
    else:
        sys.stdout.write(UNKNOWN_SITE_PACKAGES_DIR)
        sys.stdout.write(PTH_FILE)
