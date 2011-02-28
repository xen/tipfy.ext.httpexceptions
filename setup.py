"""
tipfy.ext.httpexceptions
==========================

Middleware to catch server errors and show proper page.

Setup
-----

To use this extension in your application follow few simple steps:

* Add to buildout.cfg egg import
* Modify config.py and add folowing lines::

  # Middlewares config
  config['tipfy'] = {
    'middleware': [
        # add this line to start of the list
        'tipfy.ext.httpexceptions.middleware.HTTPExceptionMiddleware',
        ..
    ]
  }

Changes
=======

0.1: Init release

"""
from setuptools import setup

setup(
    name = "tipfy.ext.httpexceptions",
    version = "0.1",
    description = 'Tipfy extension to catch 500 and 404 pages and show proper message',
    long_description = __doc__,
    zip_safe = False,
    author = 'xen',
    author_email = 'm@xen.com',
    url = 'https://github.com/xen/tipfy.ext.httpexceptions',
    packages = ['tipfy', 'tipfy.ext', 'tipfy.ext.httpexceptions' ],
    license = "BSD",
    scripts=[],
    install_requires = [
      'tipfy>=0.6, <0.7', 
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
