from setuptools import setup

setup(name='ansible_knife',
      version='0.1',
      description='Simple utility for Ansible playbook creation and download',
      url='https://github.com/ochirkov/ansible-knife.git',
      author='Chirkov Oleksandr',
      author_email='ironloriin20@gmail.com',
      license='GPLv3',
      scripts=['ansible_knife/bin/ansible-knife'],
      install_requires=[
             'gitpython',
      ],
      package_dir={ 'ansible_knife': 'ansible_knife' },
      packages=[ 'ansible_knife.helpers',
                 'ansible_knife.helpers.cvs' ],
      include_package_data=True,
      zip_safe=False)