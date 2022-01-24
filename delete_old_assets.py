# Uncomment to run sample without library built or installed on system
# import sys
# sys.path.append('/local/path/to/project/vm-console-client-python')

import rapid7vmconsole
import base64
import logging
import sys
from datetime import datetime, timedelta

max_age = 30

config = rapid7vmconsole.Configuration(name='Rapid7')
config.username = ''
config.password = ''
config.host = '' # example - https://localhost:3780
config.verify_ssl = False
config.assert_hostname = False
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

size = 30
lastPage = False
curPage = 0

while(not lastPage):
    assets = asset_api.get_assets(size=size, page=curPage)
    if len(assets.resources) < size:
        lastPage = True
    for a in assets.resources:
        last_scanned_date = a.history[-1]._date[2:].split('.', 1)[0].replace('T', ' ')
        last_scanned_date = last_scanned_date.replace('Z', '')
        last_scanned_obj = datetime.strptime(last_scanned_date, '%y-%m-%d %H:%M:%S')
        asset_age = datetime.now() - last_scanned_obj
        if asset_age.days > max_age:
            print("Asset ID: %s; Hostname: %s; IP Address: %s; Last Scan: %s" % (a.id, a.host_name, a.ip, a.history[-1]._date))
            asset_api.delete_asset(a.id)
    curPage += 1
