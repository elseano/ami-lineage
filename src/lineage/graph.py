import collections
from lineage.cloudtrail import RunInstanceMessage, CopyAmiMessage, CreateAmiMessage

CreateNode = collections.namedtuple("CreateNode", ["label", "id"])
EnsureNode = collections.namedtuple("EnsureName", ["label", "id"])
LinkNodes = collections.namedtuple("LinkNodes", ["label", "fromId", "toId"])


def determine_action(message):
    if isinstance(message, RunInstanceMessage):
        print(f"[Graph] Running actions for RunInstanceMessage: {message}")

        return [
            CreateNode("Instance", message.instanceId),
            EnsureNode("AMI", message.imageId),
            LinkNodes("LAUNCH", message.instanceId, message.imageId),
        ]

    if isinstance(message, CopyAmiMessage):
        print(f"[Graph] Running actions for CopyAmiMessage: {message}")

        return [
            CreateNode("AMI", message.sourceImageId),
            CreateNode("AMI", message.destinationImageId),
            LinkNodes("COPY", message.sourceImageId,
                      message.destinationImageId)
        ]

    if isinstance(message, CreateAmiMessage):
        print(f"[Graph] Running actions for CreateAmiMessage: {message}")

        return [
            CreateNode("Instance", message.instanceId),
            CreateNode("AMI", message.destinationImageId),
            LinkNodes("CREATE", message.instanceId, message.destinationImageId)
        ]

    return []
