"""
Backwards compatibility shim for old okpy API
"""
import os
import inspect
from okgrade.grader import grade

class Notebook:
    def __init__(self, okfile):
        """
        okfile is path to .ok file.

        This implementation does not read the .ok files.
        However, their path is used as basedir when looking
        for tests.
        """
        self.basedir = os.path.dirname(os.path.abspath(okfile))

    def auth(self, inline=False):
        """
        Legacy interface for authenticating to an okpy server.

        Not supported, so we ignore for now.
        """
        # FIXME: A warning here?
        pass

    def submit(self):
        """
        Legacy interface for submitting a notebook to okpy server.

        Not supported, so we ignore for now.
        """
        # FIXME: A warning here?
        pass

    def grade(self, question, global_env=None):
        path = os.path.join(self.basedir, "tests", "{}.py".format(question))
        if global_env is None:
            # Get the global env of our callers - one level below us in the stack
            # The grade method should only be called directly from user / notebook
            # code. If some other method is calling it, it should also use the
            # inspect trick to pass in its parents' global env.
            global_env = inspect.currentframe().f_back.f_globals
        return grade(path, global_env)