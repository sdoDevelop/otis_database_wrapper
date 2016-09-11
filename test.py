import datetime

class test1:
    x = 1


    class test2:
        y = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())



dd = test1

print(dd.test2.y)