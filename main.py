import os
from random import shuffle

from v3youtube.flow import Flow
import common.constants as Constant
import time
from concurrent.futures import ThreadPoolExecutor, wait
from common.log import setup_logging

setup_logging()

services = ["https://rapidapi.com/ytdlfree/api/youtube-v31/pricing",
            "https://rapidapi.com/ashutosh05/api/aiov-download-youtube-videos/pricing"]


def handle_rapid(position):
    flow = Flow(position=position, services=services)
    flow.generate_rapid_key()


def get_resource():
    resources = []
    path = Constant.RESOURCE_FILE
    if not os.path.isfile(path):
        raise ValueError('Resource file is required')
    with open(path, encoding="utf-8") as f:
        loaded = [x.strip() for x in f if x.strip() != '']

    for lines in loaded:
        if Constant.ERROR_MARK not in lines:
            split = lines.split(':')
            username = split[0]
            password = split[1]
            backup = split[2]
            p = f"{split[5]}:{split[6]}@{split[3]}:{split[4]}"
            resources.append({
                "proxy": p,
                "email": [
                    username,
                    password,
                    backup
                ]
            })

    resources = list(filter(None, resources))
    shuffle(resources)
    return resources


def main():
    Constant.resources = get_resource()
    num_email = len(Constant.resources)
    pool_number = list(range(num_email))
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(handle_rapid, position) for position in pool_number]
        wait(futures)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
