#!/usr/bin/env python

"""
Rabbit gestation date calculator. 31 days from rabbit sexy time.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from datetime import tzinfo, timedelta, datetime, time

def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Type Date: mm/dd/yy: ")
        try:
            d1 = datetime.strptime(userIn, "%m/%d/%y")
            isValid=True
        except:
            print "Invalid Format\n"
    return d1

endDate = ObtainDate()+timedelta(days=31)

print (endDate.strftime("%m/%d/%y"))