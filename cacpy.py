#!/usr/bin/env python
# coding:utf-8
#
# cacpy.py
#
# Author:   Hiromasa Ihara (miettal)
# Created:  2017-02-06
#
import json
import requests
from pprint import pprint as pp

API_URL='https://panel.cloudatcost.com/api'

class API() :
  def __init__(self, key, login, version="v1", api_url=API_URL) :
    self.key = key
    self.login = login
    self.version = version
    self.api_url = api_url

  def listservers(self) :
    payload = { 'key':self.key, 'login':self.login }
    ret = requests.get("{:s}/{:s}/{:s}".format(self.api_url, self.version, "listservers.php"), params=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))
    return ret_obj['data']

  def listtemplates(self) :
    payload = { 'key':self.key, 'login':self.login }
    ret = requests.get("{:s}/{:s}/{:s}".format(self.api_url, self.version, "listtemplates.php"), params=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))
    return ret_obj['data']

  def listtasks(self) :
    payload = { 'key':self.key, 'login':self.login }
    ret = requests.get("{:s}/{:s}/{:s}".format(self.api_url, self.version, "listtasks.php"), params=payload)
    print ret.text
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))
    return ret_obj['data']

  def powerop(self, sid, action) :
    payload = { 'key':self.key, 'login':self.login, 'sid':sid, 'action':action }
    ret = requests.post("{:s}/{:s}/{:s}".format(self.api_url, self.version, "powerop.php"), data=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))

  def renameserver(self) :
    pass
  def rdns(self) :
    pass
  def console(self) :
    pass
  def runmode(self) :
    pass

  def cloudpro_build(self, cpu, ram, storage, os) :
    payload = { 'key':self.key, 'login':self.login, 'cpu':cpu, 'ram':ram, 'storage':storage, 'os':os }
    ret = requests.post("{:s}/{:s}/{:s}".format(self.api_url, self.version, "cloudpro/build.php"), data=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))

  def cloudpro_delete(self, sid) :
    payload = { 'key':self.key, 'login':self.login, 'sid':sid }
    ret = requests.post("{:s}/{:s}/{:s}".format(self.api_url, self.version, "cloudpro/delete.php"), data=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))

  def cloudpro_resources(self) :
    payload = { 'key':self.key, 'login':self.login }
    ret = requests.get("{:s}/{:s}/{:s}".format(self.api_url, self.version, "cloudpro/resources.php"), params=payload)
    ret_obj = json.loads(ret.text)
    if ret.status_code != 200 :
      raise Exception("{:d} {:s}".format(ret.status_code, ret_obj["error_description"]))
    return ret_obj['data']
