from xml.etree.ElementTree import Element, SubElement, tostring


def make_xml_request(operation_name, app_name, password, lang_code, piece_code):
    xml = Element("data")
    xml.set("appname", app_name)
    xml.set("password", password)
    xml.set("request", operation_name)
    xml.set("language-code", lang_code)
    xml.set("piece-code", piece_code)
    print(tostring(xml))
    return xml

