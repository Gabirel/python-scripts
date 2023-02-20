#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys

LOG_CHOICES = {'debug':   logging.DEBUG,
               'info':    logging.INFO,
               'warning': logging.WARNING,
               'error':   logging.ERROR
               }


def setup_logging(level=logging.INFO):
    root = logging.getLogger()
    root.setLevel(level)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def setup_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level',
                        type=str,
                        default='warning',
                        choices=LOG_CHOICES,
                        help='choose a logging level. Default: warning')
    parser.add_argument('--target', help='target argument', default='', required=True)
    args = parser.parse_args()
    return args


def execute(args):
    """
    Put your main execution logic in here
    :return:
    """
    logging.debug(f'debug target: {args.target}')
    logging.info(f'info target: {args.target}')
    logging.warning(f'target: {args.target}')
    logging.error(f'log level: {args.log_level}')

    logging.warning("Try not to use `print()` use logging.")
    logging.warning("Foo executed - complex logic")


def main():
    args = setup_arguments()

    setup_logging(level=LOG_CHOICES[args.log_level])

    execute(args)
    pass


"""
Put your program instructions here

Usage:
    python3 main.py --target <target_xxx> --log-level=debug
"""
if __name__ == '__main__':
    main()
