import git
from ansible_knife.helpers import ansible_knife_exs

class Github:
    """
    Github class allows to clone repo from git or github.
    Use it for download your playbooks.
    """

    def __init__(self, **kwargs):

        self.path = kwargs.get('path')
        self.url = kwargs.get('url')

    def repo_clone(self):
        """
        Clone specified repo.
        """
        print(self.path)
        print(self.url)
        try:
            git.Git(self.path).clone(self.url)
            print('Repo was successfully downloaded.')
        except:
            raise ansible_knife_exs.GitWrongRepo('Wrong repo url or current directory exists.')