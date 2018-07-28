import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = dict()

# Publish Helper

if sys.argv[-1] == 'public':
    os.system('python setup.py sdist upload')
    sys.exit()

settings.update(
    name='inbox.py',
    version='0.0.6',
    description='SMTP for Humans',
    long_description=open('README.rst').read(),
    author='Cris Jhon',
    author_email='johncrizdoj@gmail.com',
    url='https://github.com/kennethreitz/inbox.py',
    py_modules=['inbox',],
    install_requires=['logbook', 'argparse'],
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',

    )
)

setup(**settings)