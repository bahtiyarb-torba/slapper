import os
import platform
import psutil
import ConfigParser


class SystemInfo:

    # constructor
    def __init__(self):
        pass

    @staticmethod
    def get_os_type():
        return platform.system()

    @staticmethod
    def get_memory_usage():
        return psutil.virtual_memory().total, psutil.virtual_memory().used

    @staticmethod
    def get_folder_size(directory):
        dir_size = 0
        for (path, dirs, files) in os.walk(directory):
            for filex in files:
                filename = os.path.join(path, filex)
                dir_size += os.path.getsize(filename)
        return dir_size

    @staticmethod
    def get_hostname():
        return platform.node()


class AgentConfig:

    def __init__(self, configfile='agent.config'):
        config = ConfigParser.ConfigParser()
        config.read(configfile)


class CrashReporter:    #TODO: Crash verileri ile ilgili verileri yorumlayan sinif

    def __init__(self):
        pass


class SlapperAgent:     #TODO: Sunucu tarafi ile iletisime gececek olan modul

    def __init__(self):
        pass