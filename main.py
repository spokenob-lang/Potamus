import asyncio
from core.logger import get_logger, setup_logger
from feed.binance import binance_stream
from feed.bybit import bybit_stream

# Initialize logger system
setup_logger()

logger = get_logger("SYSTEM")


async def main():
    logger.info("[INFO][SYSTEM] Potamus started")

    await asyncio.gather(
        binance_stream(),
        bybit_stream(),
    )


if __name__ == "__main__":
    asyncio.run(main())


    