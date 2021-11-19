#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import setuptools
from pathlib import Path
#from setuptools import setup
setuptools.setup(name='gym_update2',
      version='0.0.6',
      description="A OpenAI Gym Env for continuous control",
      long_description=Path("README.md").read_text(),
      long_description_content_type="text/markdown",
                 author="Claudia Viaro",
                 license="MIT",
      packages=setuptools.find_packages(include="gym_update2*"),
      install_requires=['gym']  # And any other dependencies needed
)

