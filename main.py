from v3youtube.rapid import RapidApi
import common.constants as Constant


f = open("accounts.txt", "r")
for email in f:
    RapidApi(email)



