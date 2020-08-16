import asyncio
import pytest

import aiohttp

from datetime import date
from ziggof1broadcasts import get_ziggo_f1_broadcasts

pytestmark = pytest.mark.asyncio


async def testSuccessfulCall():
    session = aiohttp.ClientSession()

    # F1 Race in Spain was on the 16th of August 2020
    startTime = date.fromisoformat('2020-08-16')

    # Test with valid startdate
    # TODO: Add test on output content
    assert await get_ziggo_f1_broadcasts(session, startTime=startTime)

    await session.close()


if __name__ == "__test__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testSuccessfulCall())