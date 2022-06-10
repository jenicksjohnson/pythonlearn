# LOGGING - making a record of the behaviour of our application.
# We keep a record of various log messages, like:
# > warning
# > debug message
# > error
# > critical error etc.

# Different log message states are:
# > info
# > debug
# > warning
# > error
# > critical

# import logging

# print(dir(logging))  # all caps - constants, first letter cap - class, all small - functions

# To create a log message, we need to create a logger object of logging class
# logger = logging.getLogger()
# print(logger)  # by default the state of the logger is 'WARNING'
# print(logger.__doc__)
# logging.basicConfig(filename='logs.log')  # create a new log file with the given name
#
# logger.info('an info message')
# logger.error('an error message')
# logger.warning('a warning message')

# There are five logging level and each level is given a value:
# > notset - 0
# > debug - 10
# > info - 20
# > warning - 30
# > error - 40
# > critical - 50
# Log messages of the current level and up are written to the log file.
# Log messages that has a lower level than the current are not written.

# logger = logging.getLogger()
# logging.basicConfig(filename='logs.log', level=logging.DEBUG)  # create a log file in DEBUG level
# logger.info('this is an info message')
# print(logger)
# print(logger.level)  # print the logging level value


# We can customize the format of the log messages using 'format' keyword.
# log_format = '%(levelname)s %(asctime)s = %(message)s'
# logger = logging.getLogger()
# logging.basicConfig(filename='logs2.log', level=logging.DEBUG, format=log_format)
# logger.info('an info message')
# logger.debug('a debug message')
# print(logger.level)

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logger = logging.getLogger()
# logging.basicConfig(filename='logs3.log', level=logging.DEBUG, format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)
# logger.warning('a warning message', extra=d)


# LOGGING AN EXCEPTION
# logger = logging.getLogger()
# logging.basicConfig(filename='log4.log', level=logging.DEBUG)
# logger.info('this is an info message')
# print(logger)
# print(logger.level)
# try:
#     a = 0
#     b = 10
#     c = b / a
# except Exception as e:
#     logger.exception(msg='Error occurred!')
#
#
#
############################################################
######################################################
#
# import logging
# myformat="%(levelname)s %(asctime)s %(message)s"
# logger=logging.getLogger("Mydemo log") #giving a name to logger(optional)
# logging.basicConfig(filename="bugs.log", level=logging.DEBUG, format= myformat )
# data= {"1111":10000,"2222":20000 }
# logger.info(data)
# class InvalidAccount(Exception):
#    pass
# class InsufficientFund(Exception):
#    pass
# def withdraw(accNo, amount):
#    logger.info(" withdraw function -start")
#    if accNo not in data:
#        logger.info( "Account Number is "+ accNo)
#        raise InvalidAccount()
#    if amount > data[accNo] :
#        logger.info("Amout is " + str(amount))
#        raise InsufficientFund()
#    data[accNo] = data[accNo]- amount
#    logger.info(" withdraw function -end")
# def main ():
#    try :
#        accNo = input("Account Number ::")
#        amount = int (input("amount"))
#        withdraw(accNo,amount)
#    except InvalidAccount as e:
#        logger.exception(e)
#    except InsufficientFund  as e:
#        logger.exception(e)
#    except ValueError  as e:
#        logger.exception(e)
#    except Exception as e :
#        logger.exception(e)
#    else :
#        pass
#    finally:
#        print("finally block")
# main()


###################################################################
#################################################################
