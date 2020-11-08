import logging

'''
DEBUG : Detailed infomation, typically of interest only when diagnosing problems

INFO : Confirmation that things are working as expected.

WARNING : An indication that something unexpected happened, or indicative of some problems in the near future (e.g 'disk space low').
The software is working as expected.

ERROR : Due to a more serious problem, the software has not been able to perform some function.

CRITICAL : A serious error, indicating that the problem itself may be unable to continue running.

'''
logging.basicConfig(filename='jj.log', level=logging.INFO)
logging.warning('Watch out')

