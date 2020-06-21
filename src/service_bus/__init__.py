try:
    VERSION = __import__("pkg_resources").get_distribution(
        "service_bus").version
except Exception:
    VERSION = "unknown"


__version__ = VERSION
