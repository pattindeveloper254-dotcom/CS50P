import asyncio
import json
import random
from datetime import datetime
from decimal import Decimal
from src.config import DATA_RAW_DIR, DEFAULT_BASE_CURRENCY

# Global currency matrices to simulate live European market flow
CURRENCY_PAIRS = ["USD", "GBP", "JPY", "CHF", "AUD", "CAD"]

async def generate_forex_tick():
    """Generates a single high-precision mock forex transaction tick."""
    target_currency = random.choice(CURRENCY_PAIRS)
    
    # Force float string casting into Decimal to completely destroy rounding bugs
    base_rate = Decimal(str(round(random.uniform(0.5, 150.0), 4)))
    fee_percentage = Decimal(str(round(random.uniform(0.001, 0.005), 5))) # 0.1% to 0.5%
    
    tick = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "base_currency": DEFAULT_BASE_CURRENCY,
        "target_currency": target_currency,
        "exchange_rate": str(base_rate),
        "transaction_fee_pct": str(fee_percentage),
        "volume": random.randint(1000, 500000)
    }
    return tick

async def run_mock_stream(duration_seconds: int = 10, interval: float = 0.5):
    """Simulates a continuous high-throughput financial streaming session."""
    print(f"🚀 Starting AeroRoute Mock Forex Stream Engine...")
    elapsed = 0.0
    
    while elapsed < duration_seconds:
        tick_data = await generate_forex_tick()
        print(f"📡 [STREAM TICK] {tick_data['base_currency']}/{tick_data['target_currency']} -> Rate: {tick_data['exchange_rate']} | Fee: {tick_data['transaction_fee_pct']}")
        
        # Non-blocking pause allows concurrent system tasks to execute freely
        await asyncio.sleep(interval)
        elapsed += interval

if __name__ == "__main__":
    # Natively kick off the asynchronous loop on execution runtime
    asyncio.run(run_mock_stream(duration_seconds=10, interval=0.5))
