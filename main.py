from v3youtube.rapid import RapidApi

import time

start_time = time.time()
f = open("accounts.txt", "r")
for email in f:
    RapidApi(email)
        

print("--- %s seconds ---" % (time.time() - start_time))



