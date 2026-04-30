import asyncio
import websockets
import orjson
from core.logger import get_logger

logger = get_logger("FEED_BYBIT")

BYBIT_WS = "wss://stream.bybit.com/v5/public/linear"

SUBSCRIBE_MSG = {
    "op": "subscribe",
    "args": ["orderbook.50.BTCUSDT"]
}

async def bybit_stream():
    while True:
        try:
            async with websockets.connect(BYBIT_WS) as ws:
                await ws.send(orjson.dumps(SUBSCRIBE_MSG).decode())
                logger.info("[INFO][FEED_BYBIT] connected")

                msg_count = 0
                start_time = asyncio.get_event_loop().time()
                last_log_time = start_time

                async for message in ws:
                    data = orjson.loads(message)
                    msg_count += 1

                    now = asyncio.get_event_loop().time()

                    if now - last_log_time >= 1:
                        rate = msg_count / (now - start_time)
                        logger.info(f"[INFO][FEED_BYBIT] msg_rate={rate:.2f}/s")
                        last_log_time = now

        except Exception as e:
            logger.error(f"[ERROR][FEED_BYBIT] {e}")
            await asyncio.sleep(2)