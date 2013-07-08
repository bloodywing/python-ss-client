#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="ss-client",
      version="9999",
      description="Dummy",
      author="jpdokter",
      author_email="",
      url="https://github.com/WickedSik/python-ss-client",
      packages=["ss_client"],
      license = "",
      install_requires=["twisted", "autobahn", "pubsub"])
