# default lib
import argparse
import os

# third party lib
import cv2

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


# global
cap = cv2.VideoCapture(0)


def cap_image():
    ret, frame = cap.read()
    if not ret:
        return False
    return frame


def getRectByPoints(points):
    # prepare simple array
    points = list(map(lambda x: x[0], points))

    points = sorted(points, key=lambda x:x[1])
    top_points = sorted(points[:2], key=lambda x:x[0])
    bottom_points = sorted(points[2:4], key=lambda x:x[0])
    points = top_points + bottom_points

    left = min(points[0][0], points[2][0])
    right = max(points[1][0], points[3][0])
    top = min(points[0][1], points[1][1])
    bottom = max(points[2][1], points[3][1])
    return (top, bottom, left, right)


def find_cards(_im):
    im_gray = cv2.cvtColor(_im, cv2.COLOR_BGR2GRAY)  # (B)
    im_blur = cv2.GaussianBlur(im_gray, (11, 11), 0)  # (C)
    im_th = cv2.threshold(im_blur, 100, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(im_th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
    # filtered with area over (all area / 100 )
    th_area = _im.shape[0] * _im.shape[1] / 100
    contours_large = list(filter(lambda c: cv2.contourArea(c) > th_area, contours))

    approxes = []

    for (i, cnt) in enumerate(contours_large):
        arclen = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * arclen, True)
        if len(approx) not in [4, 5]:
            continue
        approxes.append(approx)
    return approxes, im_blur, im_th


def classified_card(_im, card):
    pass


def main():
    logger.debug("start main func")

    while True:
        im = cap_image()
        cards, im_blur, im_th = find_cards(im)
        for i in range(len(cards)):
            cv2.drawContours(im, cards, i, (0, 255, 0), 3)

        cv2.imshow('hoge', im)
        cv2.imshow('hoge2', im_blur)
        cv2.imshow('hoge3', im_th)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    logger.debug("end main func")


if __name__ == '__main__':
    logger.debug("start __main__")
    main()
    logger.debug("end __main__")

