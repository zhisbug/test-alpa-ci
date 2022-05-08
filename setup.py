import os
from setuptools import setup

setup(
    name="test-alpa-ci",
    version=os.environ.get('VERSION')
)
