import os.path
import os

class playbook_creator:

    def __init__(self, mode, without_inventory=False, path=None, name=None, *roles):
        self.without_inventory = without_inventory
        self.mode = mode
        self.path = path
        self.name = name
        self.roles = roles
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

        # Create roles, group_vars and host_vars directories
        for i in ('group_vars', 'roles', 'host_vars'):
            self._dir_create(i)

        # Create all needed directories in roles dir
        for i in self.full_role_structure:
            dir_name = "roles/%s" % i
            self._dir_create(dir_name)

        # Create main.yml files in needed dirs
        for i in ('tasks', 'handlers', 'vars', 'meta'):
            self._file_create("".format(roles_path, i), 'main.yml')

        # Create main and inventory files
        for i in ('hosts', 'main.yml'):
            self._file_create("".format(self.path, self.name), i)