#! /usr/bin/env python3

from setuptools import setup

setup(name="python-dt3",
      version="0.5",
      description="Delta DT3-Series Temperature Controller module",
      url="https://github.com/RAA80/python-dt3",
      author="Alexey Ryadno",
      author_email="aryadno@mail.ru",
      license="MIT",
      packages=["delta"],
      install_requires=["pymodbus < 3"],
      platforms=["Linux", "Windows"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: Microsoft :: Windows",
                   "Operating System :: POSIX :: Linux",
                   "Operating System :: POSIX",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Programming Language :: Python :: 3.11",
                  ],
     )
