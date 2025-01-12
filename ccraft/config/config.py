__all__ = [
    'Config'
]

import os
import argparse as argv
import json

class Config:
    __IsInitialized = False
    __Args = None

    # Settings
    __Config = None

    def __new__(cls, *args, **kwargs):
        raise RuntimeError('%s can not be instantiated! Use class methods to interact with it.' % cls)

    @classmethod
    def initialize(cls):
        """
        Initialize class Config:
        parse command-line arguments and read config file

        Returns
        -------
        None
        """

        if cls.__IsInitialized:
            return

        cls.__parseARGV()
        cls.__changeCurDir()
        cls.__readConfigFile()

        cls.__IsInitialized = True

    @classmethod
    def __parseARGV(cls):
        Parser = argv.ArgumentParser(
            prog = 'ccraft',
            description = 'Modern automated build system for C/C++ projects, similar to GNU Make, but simpler and more powerful',
            #epilog = 'epilog'
        )

        ###
        ### Dear contributors!
        ### Please, place arguments in alphabetical order
        ###

        Parser.add_argument('-C', '--directory',
            help = 'change current working directory to DIR before doing anything',
            action = 'store',
            metavar = 'DIR',
            default = '.',
            dest = 'cwd'
        )

        Parser.add_argument('--dump-version',
            help = 'show ONLY program\'s version number and exit',
            action = 'version',
            version = '1.0.0a0'
        )

        Parser.add_argument('-v', '--version',
            action = 'version',
            version = '%(prog)s v1.0.0a0'
        )

        cls.__Args = Parser.parse_args()

    @classmethod
    def __changeCurDir(cls):
        """
        Change current working directory

        Returns
        -------
        None
        """

        if cls.__Args.cwd != '.':
            NewPath = os.path.join('.', cls.__Args.cwd)
            os.chdir(NewPath)

    @classmethod
    def __readConfigFile(cls):
        """
        Read config file.
        Current configuration can be accessed by Config.getConfig()

        Returns
        -------
        None
        """

        from . import version
        from packaging.version import Version

        ConfigFileName = 'ccraft.json'

        with open(ConfigFileName, 'r', encoding = 'utf-8') as ConfigFile:
            cls.__Config = json.load(ConfigFile)

        if version.CCraftVersion < Version(cls.__Config['CCraftMRV']):
            raise RuntimeError(
                'CCraft minimum required version for \"' + cls.__Config['ProjectName'] + '\" ' +
                'is ' + cls.__Config['CCraftMRV'] + '! ' +
                'Please, upgrade CCraft using pip.'
            )

    @classmethod
    def getConfig(cls) -> dict:
        """
        Get current configuration

        Returns
        -------
        dict:
            current configuration object (json)
        """

        return cls.__Config
