# python-scripts

Some useful scripts to use dailyot

# Feature List

- git-linkify: convert ssh-style to http-style
- clone: convert ssh-style to http-style, then clone it

# Usage

## git-linkify

```shell
$ ./git-linkify.py --help                                                                             21:07:07
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
```


## clone

```shell
$ ./clone.py --help                                                                             21:07:07
usage: clone.py [-h] [--username USERNAME] [--password PASSWORD] [--host-name HOST_NAME] [--log-level {debug,info,warning,error}] url

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
```
