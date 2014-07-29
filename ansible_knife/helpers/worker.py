import os
import ansible_knife.ansible_knife_exs

class playbook_creator:

    def __init__(self, **kwargs):
        self.without_inventory = kwargs.get('without_inventory')
        self.mode = kwargs.get('mode')
        self.path = kwargs.get('path')
        self.name = kwargs.get('name')
        self.roles = kwargs.get('roles')
        self.full_role_structure = ('tasks', 'handlers', 'templates', 'files', 'vars', 'meta')
        self.default_role_structure = ('tasks', 'templates', 'vars')

    # This function creates files
    def _files_create(self, path, *args):
        for i in args:
            with open(os.path.join(path, i),"a+") as f:
                f.write("# File created by ansible-knife")

    # This function creates dirs
    def _dirs_create(self, path, *args):

        for i in args:
            dir_name = os.path.join(path, i)
            os.makedirs(dir_name)

        return dir_name

    def _create_roles_dirs(self):

       # Create roles dirs
        if self.mode == 'full':
            role_struct = self.full_role_structure
        else:
            role_struct = self.default_role_structure

        for k in self.roles:
            path = os.path.join(self.path, self.name, 'roles', k)
            self._dirs_create(path, *role_struct)


    def playbook_create(self):

        if os.path.isdir(os.path.join(self.path, self.name)):
            msg = "This playbook already exists"
            raise ansible_knife_exs.PlaybookExists(msg)
        else:
            # Create playbook dir
            self._dirs_create(self.path, self.name)

            # Create role dir
            path = os.path.join(self.path, self.name)
            self._dirs_create(path, 'roles')

        # Create root meta files
        if not self.without_inventory:
            req_files = ('hosts', 'main.yml')
        else:
            req_files = ('main.yml',)
        self._files_create(path, *req_files)

        # Create extra root dirs
        if self.mode == 'full':
            for i in ('group_vars', 'host_vars'):
                self._dirs_create(path, i)

        # Create roles structure
        self._create_roles_dirs()


    def playbook_add(self):

        path = os.path.join(self.path, self.name, 'roles')
        for i in self.roles:
            if os.path.isdir(os.path.join(path, i)):
                msg = "{} role already exists. Modify request and try again".format(i)
                raise ansible_knife_exs.RoleExists(msg)

        # Add roles
        self._create_roles_dirs()


# TODO: add method for download from github