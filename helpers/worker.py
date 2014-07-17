import os.path
import os

class playbook_creator:

    def __init__(self, **kwargs):
        self.without_inventory = kwargs.get('without_inventory', False)
        self.mode = kwargs.get('mode', 'default')
        self.path = kwargs.get('path', None)
        self.name = kwargs.get('name', None)
        self.roles = kwargs.get('roles', None)
        self.full_role_structure = ('tasks', 'handlers', 'templates', 'files', 'vars', 'meta')
        self.default_role_structure = ('tasks', 'templates', 'vars')


    def _file_create(self, path, name):
        with open(os.path.join(path, name),"a+") as f:
            f.write("# File created by ansible-knife")


    def _dir_create(self, name):

        dir_name = os.path.join(self.path, self.name, name)
        os.makedirs(dir_name)

        return dir_name


    def full_playbook(self):

        roles_path = os.path.join(self.path, self.name, 'roles')

        if self.mode == 'full':
            # Create roles, group_vars and host_vars directories
            for i in ('group_vars', 'roles', 'host_vars'):
                self._dir_create(i)

        else:
            self._dir_create('roles')

        # Create all needed directories in roles dir
        for k in self.roles:
            for i in self.full_role_structure:
                dir_name = os.path.join('roles', k, i)
                self._dir_create(dir_name)

        # # Create main.yml files in needed dirs
        # for i in ('tasks', 'handlers', 'vars', 'meta'):
        #     self._file_create("".format(roles_path, i), 'main.yml')
        #
        # # Create main and inventory files
        # for i in ('hosts', 'main.yml'):
        #     self._file_create("".format(self.path, self.name), i)