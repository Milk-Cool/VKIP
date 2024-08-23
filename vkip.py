import json
import logging
from urllib.parse import parse_qs


HOST = "api.mycdn.me"
PATH = "/api/vchat/clientStats"


def request(flow):
    if flow.request.host_header == HOST and (flow.request.path == PATH or flow.request.path == PATH + "/"):
        data = json.loads(parse_qs(flow.request.text)["data"][0])
        for i in data["items"]:
            if "remote_address" in i:
                logging.info("Captured IP address: " + i["remote_address"])
                break
