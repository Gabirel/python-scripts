#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from urllib.parse import urlparse, urlsplit, urlunsplit

GIT_SEPARATOR = ':'
DEFAULT_HOST_NAME = 'github.com'
DEFAULT_URL_SCHEME = 'https'

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
    parser.add_argument('url', type=str, help='ssh-style git url. Example: git@github.com:abc/abc.git')
    parser.add_argument('--username',
                        type=str,
                        help='username for authentication')
    parser.add_argument('--password',
                        type=str,
                        help='password for authentication')
    parser.add_argument('--host-name',
                        type=str,
                        default=DEFAULT_HOST_NAME,
                        help='actual host name')
    parser.add_argument('--log-level',
                        type=str,
                        default='warning',
                        choices=LOG_CHOICES,
                        help='choose a logging level. Default: warning')
    args = parser.parse_args()
    return args


def is_url_valid(url: str):
    """
    Check whether url is valid for ssh-style
    :param url: ssh-style git url
    :return: valid status
    """
    result = urlparse(url)
    if result.scheme not in ['git']:
        return False
    return False


def env_check(args):
    username = args.username
    password = args.password
    host = args.host_name

    # check host
    if host is None:
        logging.info("host is None")
    pass

    if '.' not in host:
        logging.error(f"host not valid: {host}")
        exit(-1)
    pass

    # allow this situation
    if username is None or password is None:
        logging.info(f"username = {username}, password = {password}")
        return
    pass

    if len(username) == 0 or len(password) == 0:
        logging.error("username or password is empty")
        exit(-1)
    pass


def pre_check(url: str):
    """
    check first before use it
    :param url: ssh-style git url
    """
    if GIT_SEPARATOR not in url:
        logging.error(f"url not valid: {url}")
        exit(-1)
    pass


def convert(url: str, args):
    split = urlsplit('')

    scheme = DEFAULT_URL_SCHEME

    username = args.username
    password = args.password
    host = args.host_name
    netloc = f"{username}:{password}@{host}"

    # no username and password is needed
    if username is None or password is None:
        netloc = f"{host}"

    _, path = url.split(GIT_SEPARATOR)

    # assemble
    split = split._replace(scheme=scheme, netloc=netloc, path=path)

    new = urlunsplit(split)
    print(new)


def execute(args):
    """
    convert ssh-style to http-style
    :return:
    """
    url = args.url
    logging.info(f'info target: {url}')

    pre_check(url)

    # convert to http style
    convert(url, args)


def main():
    args = setup_arguments()

    setup_logging(level=LOG_CHOICES[args.log_level])

    env_check(args)

    execute(args)
    pass


"""
convert ssh-style git string into http-style link

usage: git-linkify.py [-h] [--username USERNAME] [--password PASSWORD] [--host-name HOST_NAME] [--log-level {debug,info,warning,error}] url

positional arguments:
  url                   ssh-style git url. Example: git@github.com:abc/abc.git

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   username for authentication
  --password PASSWORD   password for authentication
  --host-name HOST_NAME
                        actual host name
  --log-level {debug,info,warning,error}
                        choose a logging level. Default: warning
"""
if __name__ == '__main__':
    main()
