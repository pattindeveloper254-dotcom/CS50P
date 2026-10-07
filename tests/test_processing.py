import pytest
from decimal import Decimal, getcontext
from src.config import FINANCIAL_CONTEXT

def test_decimal_precision_enforcement():
    """Verify that the strict global Decimal context prevents float-rounding bugs."""
    # Ensure our financial context is active
    assert FINANCIAL_CONTEXT.prec == 28
    
    # Standard floating point math fails here: 0.1 + 0.2 = 0.30000000000000004
    # But strict Decimal tracking must evaluate exactly to 0.3
    val1 = Decimal("0.1")
    val2 = Decimal("0.2")
    result = val1 + val2
    
    assert result == Decimal("0.3")
    assert result != 0.30000000000000004

def test_financial_rounding_rules():
    """Verify that financial rounding maps strictly to HALF_UP parameters."""
    # Under ROUND_HALF_UP: 2.5 goes to 3, but 2.4 goes to 2
    context = FINANCIAL_CONTEXT
    
    num_up = Decimal("2.5").quantize(Decimal("1"), context=context)
    num_down = Decimal("2.4").quantize(Decimal("1"), context=context)
    
    assert num_up == Decimal("3")
    assert num_down == Decimal("2")
