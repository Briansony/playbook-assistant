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
            _dirs_create(self.path, self.name)

            # Create role dir
            path = os.path.join(self.path, self.name)
            _dirs_create(path, 'roles')

        # Create root meta files
        if not self.without_inventory:
            req_files = ('hosts', 'main.yml')
        else:
            req_files = ('main.yml',)
        _files_create(path, *req_files)

        # Create extra root dirs
        if self.mode == 'full':
            for i in ('group_vars', 'host_vars'):
                _dirs_create(path, i)

        # Create roles structure
        _create_roles_dirs()


    def role_create(self):

        path = os.path.join(self.path, self.name, 'roles')
        for i in self.roles:
            if os.path.isdir(os.path.join(path, i)):
                msg = "{} role already exists. Modify request and try again".format(i)
                raise ansible_knife_exs.RoleExists(msg)

        # Add roles
        _create_roles_dirs()













    def _role_struct_create(self, role_struct):

        # Create roles
        for k in self.roles:
            for i in role_struct:
                dir_name = os.path.join('roles', k, i)
                self._dir_create(dir_name)


    def _role_struct_add(self, role_struct):

        # Add roles
        # Check whether roles exist
        for k in self.roles:
            for i in role_struct:
                dir_name = os.path.join('roles', k, i)
                self._dir_create(dir_name)


    def _role_meta_files(self, meta_dirs):
        # Create main.yml files in needed dirs
        for k in self.roles:
            for i in meta_dirs:
                self._file_create(os.path.join(self.roles_path, k, i), 'main.yml')


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

        # Process roles
        self._role_struct_create(role_struct)
        self._role_meta_files(meta_file_dirs)

        # Create inventory and main playbook file
        if not self.without_inventory:
            req_files = ('hosts', 'main.yml')
        else:
            req_files = ('main.yml',)

        for i in req_files:
            self._file_create(os.path.join(self.path, self.name), i)


    def playbook_create(self):

        if os.path.isdir(os.path.join(self.path, self.name)):
            msg = "This playbook already exists"
            raise ansible_knife_exs.PlaybookExists(msg)
        else:
            # Create playbook
            self._create_meta()

# TODO: add method for new role

    def new_role(self):
        if self.mode == 'full':
            role_struct = self.full_role_structure
            meta_file_dirs = ('tasks', 'handlers', 'vars', 'meta')
        else:
            role_struct = self.default_role_structure
            meta_file_dirs = ('tasks', 'vars')

        self._role_struct_create(role_struct)
        self._role_meta_files(meta_file_dirs)


# TODO: add method for download from github