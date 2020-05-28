from lineage.cloudtrail import parse
from lineage.graph import determine_action
from lineage.gremlin import execute_all
from lineage.neptune import traversal

import gzip
import base64
import json


def lambda_handler(event, context):
    print(event)

    cloudwatch_event = event["awslogs"]["data"]
    decode_base64 = base64.b64decode(cloudwatch_event)
    log_uncompressed = gzip.decompress(decode_base64).decode("utf8")

    print(log_uncompressed)

    for log_entry in json.loads(log_uncompressed)["logEvents"]:
        log_text = log_entry["message"]

        print(log_text)

        result = parse(log_entry)

        actions = determine_action(result)
        execute_all(traversal, actions)

    return "Ok"
