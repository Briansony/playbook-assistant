from setuptools import setup

setup(name='playbook-assistant',
      version='0.1',
      description='Simple utility for Ansible playbook creation and download',
      url='https://github.com/ochirkov/playbook-assistant.git',
      author='Chirkov Oleksandr',
      author_email='ironloriin20@gmail.com',
      license='GPLv3',
      scripts=['playbook-assistant/bin/playbook-assistant'],
      install_requires=[
             'gitpython',
      ],
      package_dir={ 'playbook-assistant': 'playbook-assistant' },
      packages=[ 'playbook-assistant.helpers',
                 'playbook-assistant.helpers.cvs' ],
      include_package_data=True,
      zip_safe=False)