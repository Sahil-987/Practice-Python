import logging

logging.basicConfig(filename="logging_exception_details.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s | line no = %(lineno)s")


# ## Method-1
# try:
#     ag = int(input("Enter your Age : "))

# except Exception as e:
#     # logging.error("Exception Details : ",exc_info=True)
#     logging.exception("Exception Details : ")



## User defined Exception

class AccessDenied(Exception):
    pass


try:
    ag = int(input("Enter your age : "))

    if ag < 18:
        raise AccessDenied("Access Denied")
    logging.info(f"a user having age {ag} has logged in")

except Exception as e: 
    logging.exception("Exception Occured ")
