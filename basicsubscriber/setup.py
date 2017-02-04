from setuptools import setup

setup(name='basicsubscriber',
      version='0.1',
      description='subscriber class for basic publisher-subscriber API',
      url='https://github.com/geraldzakwan/Basic-Publish-Subscribe-API',
      author='Geraldi Dzakwan',
      author_email='geraldi.dzakwan@gmail.com',
      license='MIT',
      packages=['basicsubscriber'],
      install_requires=['zmq>=0.0.0', 'pyzmq>=16.0.2']
      )