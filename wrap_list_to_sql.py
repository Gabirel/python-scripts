#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import os.path
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
    parser.add_argument('-c',
                        '--char',
                        type=str,
                        default='\'',
                        help='the char which wraps list')
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        required=True,
                        help='target file list to wrap')
    parser.add_argument('--log-level',
                        type=str,
                        default='warning',
                        choices=LOG_CHOICES,
                        help='choose a logging level. Default: warning')
    args = parser.parse_args()
    return args


def env_check(args):
    split_char = args.char
    input_file = args.file

    if split_char is None or input_file is None:
        logging.info(f"chair or input file is None")
        exit(-1)
    pass

    if len(split_char) == 0 or len(input_file) == 0:
        logging.error("char or input file path is empty")
        exit(-1)
    pass


def execute(args):
    """
    do the execution
    """
    file_path = os.path.abspath(args.file)

    # read file
    with open(file_path, 'r') as f:
        lines = f.read().split()
    pass

    split_char = args.char
    # convert: abc -> `<char>`abc`<char>`,
    format_lines = ["{}{}{}{}".format(split_char, line, split_char, ',' if index < len(lines) - 1 else '') for
                    index, line in enumerate(lines)]
    # print
    for i in format_lines:
        print(i, end='')


def main():
    args = setup_arguments()

    setup_logging(level=LOG_CHOICES[args.log_level])

    env_check(args)

    execute(args)
    pass


"""
wrap list with some char, must use file as input

From:
```
abc
edf
```

To:
```
'abc','edf'
```

For fish:
# wrap list to sql type
function sqlwrapcopy -d "wrap list to sql type and then copy to the clipboard"
    /usr/local/bin/wrap_list_to_sql -f $argv | pbcopy; pbpaste
end

usage: wrap_list_to_sql [-h] [-c CHAR] -f FILE [--log-level {debug,info,warning,error}]

options:
  -h, --help            show this help message and exit
  -c CHAR, --char CHAR  the char which wraps list
  -f FILE, --file FILE  target file list to wrap
  --log-level {debug,info,warning,error}
                        choose a logging level. Default: warning
"""
if __name__ == '__main__':
    main()
