from setuptools import setup

setup(name = 'Babylon number manipulator',
      version = '0.0.1',
      author = 'Vasyl Kushnir',
      author_email = 'vasylll95@gmail.com',
      description = 'Module that can help to convert arabic numbers to babylon and vice verca',
      packages = ['babylon', 'tests'],
      test=['tests'],
      install_requires=['genty==1.3.2']
      )