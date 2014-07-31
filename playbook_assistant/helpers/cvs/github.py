import git
from playbook_assistant.helpers import playbook_assistant_exs

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
            raise playbook_assistant_exs.GitWrongRepo('Wrong repo url or current directory exists.')