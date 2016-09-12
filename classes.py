import sqlite3
import datetime
import os
import sys

class resource_management:
    app_folder = None
    db_folder = None
    db_file = None
    log_folder = None
    error_log = None

    def __init__(self):
        self.app_folder = os.path.expanduser("~") + "/.otis"

        # Set up any internal folders and files
        self.db_folder = self.app_folder + "/db"
        self.db_file = self.db_folder + "/otis_db.sqlite"
        self.log_folder = self.app_folder + "/logs"
        self.error_log = self.log_folder + "/error_log.txt"

        target = self.log_folder
        if not os.path.exists(target):
            os.makedirs(target)
        thefile = open(self.error_log,"w")
        thefile.write("__--__Error Log__--__")
        thefile.write(os.linesep)
        thefile.write(os.linesep)


class errario:
    error_log = []
    error_log_queue = []
    resources = resource_management()

    class ind_error:
        time = ""
        error_code = []
        facility = None
        message = None
        stack_trace = None
        log_string = None


        def __init__(self,p_error_code=None,p_facility=None,p_message=None,p_stack_trace=None):
            # Set the error variables to these
            self.time = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            self.error_code = p_error_code
            self.facility = p_facility
            self.message = p_message
            self.stack_trace = p_stack_trace

            self.create_string()

        def create_string(self):
            s="[Time:" + self.time + "]"
            s=s + " {" + self.error_code + " | " + self.facility + "}"
            s=s + " *Message: " + self.message
            self.log_string = s
            return self.log_string


    def go(self,err=ind_error):
        # log error to memory
        self.error_log.append(err.create_string())

        # write to file
        string = err.create_string()
        thefile = open(self.resources.error_log, "a")
        thefile.write(string)





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