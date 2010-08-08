import setuptools

setuptools.setup(name='pytest-cov',
                 version='1.2',
                 description='py.test plugin for coverage reporting with support for both centralised and distributed testing, including subprocesses',
                 long_description=open('README.txt').read().strip(),
                 author='Meme Dough',
                 author_email='memedough@gmail.com',
                 url='http://bitbucket.org/memedough/pytest-cov/overview',
                 py_modules=['pytest_cov'],
                 install_requires=['py>=1.3.3',
                                   'pytest-xdist>=1.4',
                                   'cov-core>=1.1'],
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
