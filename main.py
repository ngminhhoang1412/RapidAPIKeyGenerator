from v3youtube.rapid import RapidApi

import time


if __name__ == '__main__':
    start_time = time.time()
    a = RapidApi()
    a.generator()

    print("--- %s seconds ---" % (time.time() - start_time))
