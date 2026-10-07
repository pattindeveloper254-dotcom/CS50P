class AeroRouteException(Exception):
    """Base system error exception for the AeroRoute engine track."""
    pass

class NetworkTimeoutError(AeroRouteException):
    """Triggered when connection boundaries drop out during mock streaming fetches."""
    pass

class InsufficientLiquidityError(AeroRouteException):
    """Triggered when calculated transaction cost margins violate target constraints."""
    pass
