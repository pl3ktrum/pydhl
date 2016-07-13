from xml.etree.ElementTree import tostring
from pydhl import requestbuilder, config

# TEST
print(tostring(requestbuilder.make_xml_request("test", "app name jo", "password jo", "language code jo", "pimmel code jo")))