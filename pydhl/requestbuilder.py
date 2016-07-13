from xml.etree.ElementTree import Element, SubElement


def make_xml_request(operation_name, app_name, password, lang_code, piece_code):
    xml = Element("data")
    SubElement(xml, "appname").text = app_name
    SubElement(xml, "password").text = password
    SubElement(xml, "request").text = operation_name
    SubElement(xml, "language-code").text = lang_code
    SubElement(xml, "piece-code").text = piece_code
    return xml
