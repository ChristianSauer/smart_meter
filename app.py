import asyncio
import datetime
import time
import typing

import serial
from smlpy import data_reader
from loguru import logger
from smlpy.sml_reader import SmlGetListRes, SmlValListEntry

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
        logger.info("reading data")
        port_settings = data_reader.PortSettings(
            port="/dev/ttyUSB0",
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            wait_time=data_reader.WAIT_TIME,
        )

        # todo catch end but no start errors
        try:
            result = await data_reader.read_one(port_settings)

            val_data = result.data[1].message_body
            val_data: SmlGetListRes
            values = val_data.val_list
            values: typing.List[SmlValListEntry]

            results = {x.obj_name: x.get_scaled_value() for x in values if type(x.value) == int}
            tags = {x.obj_name: x.unit for x in values if type(x.value) == int}

            _ravendb.store_result(results, tags)
            _delay_for_timeout_seconds()
        except Exception:
            logger.exception("Unexpected error")
            continue


if __name__ == '__main__':
    asyncio.run(run())
