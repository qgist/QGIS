# -*- coding:utf-8 -*-
"""
/***************************************************************************
                            Plugin Installer module
                             -------------------
    Date                 : March 2020
    Copyright            : (C) 2020 by Sebastian M. Ernst
    Email                : ernst at pleiszenburg dot de

    This module is based on two former plugin_installer plugins:
      Copyright (C) 2007-2008 Matthew Perry
      Copyright (C) 2008-2013 Borys Jurgiel
      Copyright (C) 2020 Sebastian M. Ernst

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

"""
- One file per class?
- Auto-detect (and auto-import) repo types
"""

class Settings:
    """
    Transparent wrapper around QgsSettings - so it can be exchanged (for testing etc)
    """

class Index:
    """
    # Index of repos

    - properties:
        - list of present/registered repos
        - allow experimental
        - allow deprecated
        - SETTINGS
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
        - writeable (FALSE for core plugins)
        - autorefresh (on start)
        - autorefresh_interval
        - AUTH?
        - priority
        - available (i.e. contact to server?)
        - meta ...
        - LIST OF PLUGINS
        - SETTINGS
    """
    def get_all_installed(self):
        pass
    def get_all_available(self):
        """
        Available plugins, compatible to QGIS version
        """
    def rename(self, new_name):
        pass
    def refresh(self):
        pass
    def _fetch_index(self):
        """HTTP ..."""
        pass
    @classmethod
    def from_directory(cls, path, writeable = False):

        return cls()

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
        - upgradable
        - downgradable
        - orphan
        - meta ...
        - Caches
        - SETTINGS
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
        Filter versions compatible to QGIS version
        """
        pass
    def send_vote(self):
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
