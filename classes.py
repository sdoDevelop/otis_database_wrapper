import sqlite3
import datetime
import os
import sys

class resource_management:
    # Set up the initial app folder directory dependant on os
    """
    from sys import platform
    if platform == "linux" or platform == "linux2":
        # Linux
        app_folder = "/usr/local/lib/otis/"
    elif platform == "darwin":
        # OS X
        app_folder = "Library/Application support/"
    elif platform == "win32":
        # Windows
        app_folder = ""
    """

    app_folder = ""
    db_folder = ""
    db_file = ""
    log_folder = ""
    error_log = ""

    def __init__(self,dill):
        app_folder = os.path.expanduser("~") + "/.otis"

        # Set up any internal folders and files
        db_folder = app_folder + "/db"
        db_file = db_folder + "/otis_db.sqlite"
        log_folder = app_folder + "/logs"
        error_log = log_folder + "/error_log.txt"

        target = resource_management.log_folder
        if not os.path.exists(target):
            os.makedirs(target)
        thefile = open(target,"w")
        thefile.write("__--__Error Log__--__")
        thefile.write(os.linesep)
        thefile.write(os.linesep)


class errario:
    error_log = []
    error_log_queue = []

    class ind_error:
        time = ""
        error_code = []
        facility = ""
        message = ""
        stack_trace = ""

        def __init__(self,p_error_code=None,p_facility=None,p_message=None,p_stack_trace=None):
            # Set the error variables to these
            self.time = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            self.error_code = p_error_code
            self.facility = p_facility
            self.message = p_message
            self.stack_trace = p_stack_trace

    def go(self,err):
        # log error to memory
        #self.error_log.append(err)

        # write to file
        target = classes.resource_management.error_log
        if not os.path.exists(target):
            os.makedirs(target)


        string = raw_input("brother motha fucking ali")
        thefile = open(target, 'w')
        thefile.write("brother motha fucking ali/n")
        thefile.close()






    def alert_user(self,err):
        # bring up a window for the error sent
        pass


class sqlite_database:
    pass


class postgresql_database:
    pass


class otis_db:
    local_db = sqlite3
    remote_db = "postgres"
    triggers = "none"

    def connect(self):
        try:
            conn = local_db.connect(db_file)
        except e:
            raise enumerate
        finally:
            pass

    def sql_execue(self):
        pass

    def sql_select(self):
        pass