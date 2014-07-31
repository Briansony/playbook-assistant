class AnsibleKnifeError(Exception):
    ''' The base AnsibleKnife exception from which all others should subclass '''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class PlaybookExists(AnsibleKnifeError):
    pass

class RoleExists(AnsibleKnifeError):
    pass

class GitWrongRepo(AnsibleKnifeError):
    pass