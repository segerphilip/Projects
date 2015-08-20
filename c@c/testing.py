import urllib2
import json
import os

API = os.environ.get('CLOUDATCOST_KEY')
LOGIN = os.environ.get('GMAIL1')
LINK = 'https://panel.cloudatcost.com/api/v1/'

def listServers():
  status = json.loads(urllib2.urlopen(LINK + 'listservers.php?key=' + API + '&login=' + LOGIN + '&ip_bypass=true').read())
  # TODO: parse json to get dict of running servers
  return status

def getProResources():
  # dictionary for saving resources
  proResources = {}
  resources = json.loads(urllib2.urlopen(LINK + 'cloudpro/resources.php?key=' + API + '&login=' + LOGIN + '&ip_bypass=true').read())
  # parse json and save into new resources dictionary
  proResources['cpuTotal'] = int(resources['data']['total']['cpu_total'])
  proResources['storageTotal'] = int(resources['data']['total']['storage_total'])
  proResources['ramTotal'] = int(resources['data']['total']['ram_total'])
  proResources['cpuUsed'] = int(resources['data']['used']['cpu_used'])
  proResources['storageUsed'] = int(resources['data']['used']['storage_used'])
  proResources['ramUsed'] = int(resources['data']['used']['ram_used'])
  return proResources

def removeProSever():
  urllib2.urlopen(LINK + )

# def printProResources(resources):
#   for i in resources:
#     for j in resources[i]:
#       if 'Total' in j:
#         print j
#   return None

if __name__ == '__main__':
  # print listServers()
  proResources = getProResources()
  # print proResources
  print printProResources(proResources)
