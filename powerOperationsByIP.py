#!/usr/bin/env python
# coding:utf-8
#
# powerOperationsByIP.py
#
# Author:   Hiromasa Ihara
# Created:  2017-02-06
#

import sys
import ConfigParser
import cacpy

def printUsage() :
  print "invalid number of arguments"
  print "usage: python {:s} <server_ip> <action>".format(sys.argv[0])
  print "action: poweron,poweroff,reset"
  print "server_ip: ",
  servers = api.listservers()
  for server in servers :
    print "{:s},".format(server['ip']),
  print

if __name__ == '__main__':
# perse config.ini
  config = ConfigParser.SafeConfigParser()
  config.read('cacpy.ini')
  key = config.get('settings', 'key')
  login = config.get('settings', 'login')
  api = cacpy.API(key=key, login=login, version="v1")
  servers = api.listservers()

# argument check
  if len(sys.argv) != 3 :
    printUsage()
    sys.exit(1)
  server_ip = sys.argv[1]
  action = sys.argv[2]

# arguemnt(action) check
  if action not in ['poweron', 'poweroff', 'reset'] :
    printUsage()
    sys.exit(1)

# arguemnt(server_ip) check
  if server_ip not in [server['ip'] for server in servers] :
    printUsage()
    sys.exit(1)

# do it!
  sid = [server['sid'] for server in servers if server['ip'] == server_ip][0]
  api.powerop(sid, action)
  print "success"
