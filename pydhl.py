from xml.etree.ElementTree import Element, SubElement, tostring
from . import config
import requests


def make_xml_request(operation_name, app_name, password, lang_code, piece_code):
    xml = Element("data")
    SubElement(xml, "appname").text = app_name
    SubElement(xml, "password").text = password
    SubElement(xml, "request").text = operation_name
    SubElement(xml, "language-code").text = lang_code
    SubElement(xml, "piece-code").text = piece_code
    return xml


def make_api_call():
    pass



#TEST
print(tostring(make_xml_request("test", "app name jo", "password jo", "language code jo", "pimmel code jo")))