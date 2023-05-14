from setuptools import setup, find_namespace_packages

setup(name = 'clean_folder',
      version='1.0',
      url='',
      author='Ivan Ishchenko',
      author_email='lvan.lshchenko19.01@gmail.com',
      packages=find_namespace_packages(),
      entry_points={"console_scripts": ['clean-folder=clean_folder.clean:sorting']}
      )