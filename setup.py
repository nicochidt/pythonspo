from setuptools import setup, find_packages
from spso.version import __version__, __author__, __email__, __license__
import os

desc = "Simple particle swarm optimizer in python"


setup( name                 = 'spso',
       version              = __version__,
       description          = desc,
       long_description     = desc,
       long_description_content_type = 'text/plain',
       author               = __author__,
       author_email         = __email__,
       url                  = 'http://www.github.com/nicochidt/pythonspo',
       packages             = find_packages(),
       scripts              = [],
       license              = __license__,
       classifiers          = [
            'Programming Language :: Python :: 3',
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Environment :: Console',
      ],
)
