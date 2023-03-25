import logging


def setup_logging(logfile):
    """Setup logging to a file and console."""
    logging.basicConfig(
        filename=logfile,
        level=logging.ERROR,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )