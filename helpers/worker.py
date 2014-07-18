import os
import ansible_knife_exs

class playbook_creator:

    def __init__(self, **kwargs):
        self.without_inventory = kwargs.get('without_inventory', False)
        self.mode = kwargs.get('mode', 'default')
        self.path = kwargs.get('path', None)
        self.name = kwargs.get('name', None)
        self.roles = kwargs.get('roles', None)
        self.full_role_structure = ('tasks', 'handlers', 'templates', 'files', 'vars', 'meta')
        self.default_role_structure = ('tasks', 'templates', 'vars')
        self.roles_path = os.path.join(self.path, self.name, 'roles')

    def _file_create(self, path, name):
        with open(os.path.join(path, name),"a+") as f:
            f.write("# File created by ansible-knife")


    def _dir_create(self, name):

        dir_name = os.path.join(self.path, self.name, name)
        os.makedirs(dir_name)

        return dir_name

    def _create_meta(self):

        # Create group_vars and host_vars dirs
        if self.mode == 'full':
            for i in ('group_vars', 'host_vars'):
                self._dir_create(i)

            role_struct = self.full_role_structure
            meta_file_dirs = ('tasks', 'handlers', 'vars', 'meta')
        else:
            role_struct = self.default_role_structure
            meta_file_dirs = ('tasks', 'vars')

        # Create roles with roles meta
        for k in self.roles:
            for i in role_struct:
                dir_name = os.path.join('roles', k, i)
                self._dir_create(dir_name)

        # Create main.yml files in needed dirs
        for k in self.roles:
            for i in meta_file_dirs:
                self._file_create(os.path.join(self.roles_path, k, i), 'main.yml')

        # Create inventory and main playbook file
        for i in ('hosts', 'main.yml'):
            self._file_create(os.path.join(self.path, self.name), i)

    def playbook_create(self):

        if os.path.isdir(os.path.join(self.path, self.name)):
            msg = "This playbook already exists"
            raise ansible_knife_exs.PlaybookExists(msg)
        else:
            # Create playbook
            self._create_meta()