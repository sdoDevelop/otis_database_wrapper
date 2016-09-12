import classes
import sys

#err = classes.errario.ind_error(2, "osjf", "lasjdofje", "asodfjsd")
#classes.errario.go("",err)

print(classes.resource_management.error_log)

import os



newpath = classes.resource_management.error_log
if not os.path.exists(newpath):
    os.makedirs(newpath)