import os
from decimal import Context, setcontext

# Universal setup that bypasses experimental Python 3.14 breaking changes
FINANCIAL_CONTEXT = Context(prec=28, rounding='ROUND_HALF_UP')
setcontext(FINANCIAL_CONTEXT)

# Absolute path tracking matching your QuantDev laboratory structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_OUTPUT_DIR = os.path.join(BASE_DIR, "data", "outputs")

DEFAULT_BASE_CURRENCY = "EUR"
