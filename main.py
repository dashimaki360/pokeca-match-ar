# default lib
import argparse
import os

# third party lib

# your lib

# logger setup
import logging
from logging import getLogger, StreamHandler, Formatter
logger_name = "Pokeca-AR"
logger = getLogger(logger_name)
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)

# parse args
parser = argparse.ArgumentParser(description='This script is XXX')
parser.add_argument('--XXX', help='XXX')
parser.add_argument('--YYY', type=int, default=12345, help='YYY')
parser.add_argument('-Z', '--ZZZ', default="012345", help='ZZZ')
args = parser.parse_args()


def cap_image():
    im = 0
    return im


def find_cards(_im):
    return [0, 1, 2, 3, 4]


def classified_card(card):
    return "hoge"


def main():
    logger.debug("start main func")
    im = cap_image()
    cards = find_cards(im)
    for card in cards:
        classified_card(card)
    logger.debug("end main func")


if __name__ == '__main__':
    logger.debug("start __main__")
    main()
    logger.debug("end __main__")

