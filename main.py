from pydhl.requestbuilder import make_xml_request
from pydhl import config
from requests.auth import HTTPBasicAuth
import requests


def test():
    xml = make_xml_request(operation_name="get-status-for-public-user",
                           app_name=config.KEY_TNTUSER,
                           password=config.KEY_TNTPASSWORD,
                           lang_code="de",
                           piece_code="00340434123393551147")

    headers = {'Content-Type': 'application/xml'}
    response = requests.post(config.SANDBOXURL, data=xml, headers=headers, auth=HTTPBasicAuth(config.KEY_TNTUSER,
                                                                                              config.KEY_TNTPASSWORD))
    print(response.content)


if __name__ == "__main__":
    test()
