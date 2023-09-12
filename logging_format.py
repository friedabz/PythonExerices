import logging

logging.basicConfig(
    forma='%(asctime)s %(levelname)-8s %(message)s',
    level=loffing.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.warning("my message")