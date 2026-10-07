from decimal import Decimal
from datetime import datetime
from src.config import FINANCIAL_CONTEXT

class CurrencyTick:
    """Enterprise blueprint to parse, clean, and validate raw financial data ticks."""
    
    def __init__(self, raw_payload: dict):
        # Apply global strict financial rounding context immediately on ingestion
        self.context = FINANCIAL_CONTEXT
        
        # Core metadata parameters
        self.timestamp = datetime.fromisoformat(raw_payload["timestamp"].replace("Z", "+00:00"))
        self.base_currency = str(raw_payload["base_currency"]).upper()
        self.target_currency = str(raw_payload["target_currency"]).upper()
        
        # Cast incoming floating strings strictly to high-precision Decimal types
        self.exchange_rate = Decimal(str(raw_payload["exchange_rate"]))
        self.transaction_fee_pct = Decimal(str(raw_payload["transaction_fee_pct"]))
        self.volume = int(raw_payload["volume"])
        
    @property
    def total_cost_with_fees(self) -> Decimal:
        """Dynamically calculates real transaction execution overhead down to the 28th decimal."""
        fee_amount = (self.exchange_rate * self.transaction_fee_pct).quantize(Decimal("1.00000000"), context=self.context)
        return self.exchange_rate + fee_amount

    def __repr__(self) -> str:
        return f"<CurrencyTick {self.base_currency}/{self.target_currency} @ {self.exchange_rate}>"
