# -*- coding:utf-8 -*-

"""
- One file per class?
- Auto-detect (and auto-import) repo types
"""


class Index:
    """
    # Index of repos

    - properties:
        - list of present/registered repos
    """
    def add_repo(self, **kwargs):
        pass
    def remove_repo(self, **kwargs):
        pass
    def get_repos(self, **kwargs):
        """Get list/iterator, filter for enabled, available, ..."""
        pass
    def refresh_repos(self):
        """Reload index of every repo"""
        pass

class Repository:
    """
    # Repo

    This is abstract class representing a repository.
    From this, classes for repo types (i.e. plugin sources) are derived.

    - sources:
        - remote (HTTP, FTP, ...)
        - locally (drive, share, path)
        - "links" (`ln -s`) to local folders for plugins
    - types:
        - pip (through pip API)
        - conda (through conda API)
        - traditional QGIS
    - properties:
        - NAME
        - active/enabled
        - priority
        - available (i.e. contact to server?)
        - meta ...
    """
    def refresh(self):
        pass
    def _fetch_index(self):
        """HTTP ..."""
        pass

class Plugin:
    """
    # One single plugin

    This is abstract class representing a plugin.
    From this, classes for plugin types (i.e. plugin sources) are derived?
    Or use repo type classes instead instead of having multiple plugin classes?

    - Dependencies:
        - inter-plugin
        - plugin to python packages (through source / other package manager)
    - Properties:
        - NAME / ID
        - Installed
        - Installed version
        - Available versions (from sources ...)
        - meta ...
        - Caches
    """
    def install(self):
        """
        Allows dry runs
        """
        pass
    def uninstall(self):
        """
        Allows dry runs
        """
        pass
    def upgrade(self, version):
        """
        Allows dry runs
        Also allows intentional downgrades
        """
        pass
    def get_versions(self):
        """
        Get versions of plugin
        """
        pass
    def _fetch_available_versions(self):
        """HTTP ..."""
        pass
    def _fetch_plugin(self):
        """HTTP ..."""
        pass
    def _fetch_metadata(self):
        """HTTP ..."""
        pass
    def _validate_install(self):
        """
        Post-install or post-update/-downgrade checks of files and folders
        """
        pass
    def _validate_uninstall(self):
        """
        Post-uninstall checks of files and folders
        """
        pass
