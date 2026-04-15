import re

with open('/home/jean/.openclaw/workspace/Tilos-Radio-addon-for-codi26/addon.xml', 'r') as f:
    xml_data = f.read()

xml_data = xml_data.replace('<import addon="xbmc.python" version="2.1.0"/>', '<import addon="xbmc.python" version="3.0.0"/>')

with open('/home/jean/.openclaw/workspace/Tilos-Radio-addon-for-codi26/addon.xml', 'w') as f:
    f.write(xml_data)

with open('/home/jean/.openclaw/workspace/Tilos-Radio-addon-for-codi26/addon.py', 'r') as f:
    code = f.read()

# Replace imports
code = code.replace('from urllib2 import Request, urlopen, URLError', 'from urllib.request import Request, urlopen\nfrom urllib.error import URLError')
code = code.replace('import urlparse', 'import urllib.parse')
code = code.replace('from HTMLParser import HTMLParser', 'from html.parser import HTMLParser')

# Replace urllib.urlencode -> urllib.parse.urlencode
code = code.replace('urllib.urlencode', 'urllib.parse.urlencode')
code = code.replace('urlparse.parse_qs', 'urllib.parse.parse_qs')

# Replace exceptions
code = re.sub(r'except URLError,\s*e:', 'except URLError as e:', code)
code = re.sub(r'except Exception,\s*e:', 'except Exception as e:', code)

# Replace unicode string types
code = code.replace('type(msg) not in (str, unicode):', 'type(msg) not in (str,):')
code = code.replace('type(msg) in (unicode,):', 'type(msg) in (str,):')
code = code.replace('msg = msg.encode(\'utf-8\')', '# msg = msg.encode(\'utf-8\')')

# Replace string encoding helper
code = code.replace('return string.encode(\'utf8\')', 'return str(string)')

with open('/home/jean/.openclaw/workspace/Tilos-Radio-addon-for-codi26/addon.py', 'w') as f:
    f.write(code)

print("Migration script executed.")
