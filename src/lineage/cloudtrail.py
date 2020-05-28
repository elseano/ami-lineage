import json


class RunInstanceMessage:
    pass


class CopyAmiMessage:
    pass


class CreateAmiMessage:
    pass


def parse(data):
    try:
        j = json.loads(data)
    except Exception:
        return None

    t = j["eventName"]

    if t == "RunInstances":
        result = RunInstanceMessage()
        result.region = j["awsRegion"]
        result.instanceId = j["responseElements"]["instancesSet"]["items"][0]["instanceId"]
        result.imageId = j["responseElements"]["instancesSet"]["items"][0]["imageId"]
        result.accountId = j["responseElements"]["instancesSet"]["items"][0]["ownerId"]

        return result

    if t == "CopyImage":
        result = CopyAmiMessage()
        result.region = j["awsRegion"]
        result.sourceImageId = j["requestParameters"]["sourceImageId"]
        result.destinationImageId = j["responseElements"]["imageId"]
        result.accountId = j["recipientAccountId"]

        return result

    if t == "CreateImage":
        result = CreateAmiMessage()
        result.region = j["awsRegion"]
        result.instanceId = j["requestParameters"]["instanceId"]
        result.destinationImageId = j["responseElements"]["imageId"]
        result.accountId = j["recipientAccountId"]

        return result

    return None
