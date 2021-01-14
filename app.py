import asyncio
import codecs
import datetime
import time

import smlpy
from loguru import logger
import _cfg
import _ravendb

config = _cfg.config


def _delay_for_timeout_seconds():
    next_run = datetime.datetime.utcnow() + datetime.timedelta(seconds=config.timeout)
    wait_time = next_run - datetime.datetime.utcnow()
    seconds = wait_time.total_seconds()
    logger.info("Waiting until {next_run} -> {seconds} seconds", next_run=next_run, seconds=seconds)

    time.sleep(seconds)



async def run():
    while True:
        result = smlpy.
        _delay_for_timeout_seconds()


if __name__ == '__main__':
    asyncio.run(run())
