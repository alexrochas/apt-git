from setuptools import setup

setup(name='apt_git',
      version='0.1',
      description='Apt-get like tool for github repositories',
      url='https://github.com/alexrochas/apt-git',
      author='Alex Rocha',
      author_email='alex.rochas@yahoo.com.br',
      license='MIT',
      packages=['apt_git'],
      install_requires=['requests==2.10.0'],
      entry_points={
          'console_scripts': ['apt-git=apt_git.console:main'],
      },
      include_package_data=True,
      zip_safe=False)