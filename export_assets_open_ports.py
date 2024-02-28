# Uncomment to run sample without library built or installed on system
# import sys
# sys.path.append('/local/path/to/project/vm-console-client-python')

import rapid7vmconsole
import base64
import logging
import sys
import csv
from datetime import datetime, timedelta

max_age = 30
# Specify ID of Site, from which you want to delete assets
# If left None, assets from all sites will be deleted (older than max_age)
site_id = 52

config = rapid7vmconsole.Configuration(name='Rapid7')
config.username = ''
config.password = ''
config.host = '' # example - https://localhost:3780
config.verify_ssl = False
config.assert_hostname = False
config.ignore_scan_types = [''] # example - ['ASSET-IMPORT', 'SCAN']
config.proxy = None
config.ssl_ca_cert = None
config.connection_pool_maxsize = None
config.cert_file = None
config.key_file = None
config.safe_chars_for_path_param = ''

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
logger.addHandler(ch)
config.debug = False


auth = "%s:%s" % (config.username, config.password)
auth = base64.b64encode(auth.encode('ascii')).decode()
client = rapid7vmconsole.ApiClient(configuration=config)
client.default_headers['Authorization'] = "Basic %s" % auth
asset_api = rapid7vmconsole.AssetApi(client)
site_api = rapid7vmconsole.SiteApi(client)

size = 30
lastPage = False
curPage = 0

fields = ['ip', 'port', 'name', 'product']

with open(".//open_ports.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    while(not lastPage):
        assets = None
        if (site_id != None):
            assets = site_api.get_site_assets(site_id, size=size, page=curPage, sort=["ip"])
        else:
            assets = asset_api.get_assets(size=size, page=curPage, sort=["ip"])
        if len(assets.resources) < size:
            lastPage = True
        for a in assets.resources:
            if (a.services != None):
                for service in a.services:
                    service_row = [{
                        'ip': a.ip,
                        'name': service.name,
                        'port': str(service.port) + '/' + service.protocol.upper(),
                        'product': service.product
                    }]
                    writer.writerows(service_row)
            else:
                service_row = [{
                    'ip': a.ip
                }]
                writer.writerows(service_row)
        curPage += 1
