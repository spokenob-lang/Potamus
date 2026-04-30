import asyncio
import websockets
import orjson
from core.logger import get_logger

logger = get_logger("FEED_BINANCE")

BINANCE_WS = "wss://stream.binance.com:9443/ws/btcusdt@depth@100ms"

async def binance_stream():
    while True:
        try:
            async with websockets.connect(BINANCE_WS) as ws:
                logger.info("connected")

                msg_count = 0
                start_time = asyncio.get_event_loop().time()

                async for message in ws:
                    data = orjson.loads(message)
                    msg_count += 1

                    # Log every 100 messages (avoid spam)
                    if msg_count % 100 == 0:
                        elapsed = asyncio.get_event_loop().time() - start_time
                        rate = msg_count / elapsed if elapsed > 0 else 0
                        logger.info(f"msg_rate={rate:.2f}/s")

        except Exception as e:
            logger.error(f"error: {e}")
            await asyncio.sleep(2)  # reconnect delay