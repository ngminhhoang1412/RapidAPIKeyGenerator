import os
import sys
from random import shuffle

from v3youtube.rapid import RapidApi
import common.constants as Constant
import time
from concurrent.futures import ThreadPoolExecutor, wait
from common.log import setup_logging

setup_logging()


def handle_rapid(position):
    rapid = RapidApi(position)
    rapid.generate_key()


def get_gmail_list():
    gmail_filename = Constant.gmail_file_name
    gmails = []

    if not os.path.isfile(gmail_filename) and gmail_filename[-4:] != '.txt':
        gmail_filename = f'{gmail_filename}.txt'

    try:
        with open(gmail_filename, encoding="utf-8") as fh:
            loaded = [x.strip() for x in fh if x.strip() != '']
    except Exception:
        sys.exit()

    for lines in loaded:
        if lines.count(':') == 2:
            split = lines.split(':')
            username = split[0]
            password = split[1]
            backup = split[2]
            gmails.append([
                username,
                password,
                backup
            ])
        elif lines.count(':') == 1:
            split = lines.split(':')
            username = split[0]
            password = split[1]
            gmails.append([
                username,
                password,
                "empty"
            ])

    gmails = list(filter(None, gmails))
    shuffle(gmails)
    return gmails


def main():
    Constant.gmail_list = get_gmail_list()
    num_email = len(Constant.gmail_list)
    pool_number = list(range(num_email))
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(handle_rapid, position) for position in pool_number]
        wait(futures)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
