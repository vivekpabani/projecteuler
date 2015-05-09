#!/usr/bin/env python

"""
Problem Definition :

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The answer of these
multiples is 23. Find the answer of all the multiples of 3 or 5 below 1000.

"""
import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():

    start_time = time.clock()

    logger.info('Initializing answer.')
    answer = 0
    logger.debug("answer : %d", answer)

    logger.info('Starting loop.')
    for x in xrange(1, 1000):
        logger.debug("Iteration : %d", x)

        if x % 3 == 0:
            answer += x
            logger.debug("Added to answer : %d Answer : %d", x, answer)
        elif x % 5 == 0:
            answer += x
            logger.debug("Added to answer : %d Answer : %d", x, answer)

    logger.info('Out of loop.')

    logger.debug("Final answer : %d ", answer)
    print answer

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':

    main()
