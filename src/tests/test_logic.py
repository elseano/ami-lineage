import collections

from lineage.cloudtrail import RunInstanceMessage, CopyAmiMessage, CreateAmiMessage
from lineage.graph import *


def test_run_instance():
    input = RunInstanceMessage()
    input.instanceId = "INSTANCEID"
    input.imageId = "IMAGEID"

    result = determine_action(input)

    assert result == [
        CreateNode("Instance", "INSTANCEID"),
        EnsureNode("AMI", "IMAGEID"),
        LinkNodes("LAUNCH", "INSTANCEID", "IMAGEID")
    ]


def test_create_ami():
    input = CreateAmiMessage()
    input.instanceId = "INSTANCE1"
    input.destinationImageId = "AMI1"

    result = determine_action(input)

    assert result == [
        CreateNode("Instance", "INSTANCE1"),
        CreateNode("AMI", "AMI1"),
        LinkNodes("CREATE", "INSTANCE1", "AMI1")
    ]


def test_copy_ami():
    input = CopyAmiMessage()
    input.sourceImageId = "AMI1"
    input.destinationImageId = "AMI2"

    result = determine_action(input)

    assert result == [
        CreateNode("AMI", "AMI1"),
        CreateNode("AMI", "AMI2"),
        LinkNodes("COPY", "AMI1", "AMI2")
    ]
