import svn

from svn import common


class RemoteClient(common.CommonClient):
    def __init__(self, path, *args, **kwargs):
        super(RemoteClient, self).__init__(path, svn.T_URL, *args, **kwargs)

    def checkout(self, path):
        self.run_command('checkout', [self.url, path])

    def __repr__(self):
        return ('<SVN(REMOTE) %s>' % (self.url))
