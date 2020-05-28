from lineage.cloudtrail import parse


def test_invalid_json():
    result = parse("blah")
    assert result is None


def test_dont_understand():
    result = parse("{ 'someJSON': true }")
    assert result is None


def test_run_instances():

    result = parse("""{
      "eventSource": "ec2.amazonaws.com",
      "eventName": "RunInstances",
      "awsRegion": "us-west-2",
      "responseElements": {
        "instancesSet": {
          "items": [
            {
              "instanceId": "i-0f94de47f90462018",
              "imageId": "ami-0ce21b51cb31a48b8",
              "ownerId": "527579490183"
            }
          ]
        }
      },
      "requestID": "3dc68d64-9435-4c46-9562-1e3272747cbe",
      "eventID": "f3902997-b8f3-40c2-8f3a-403f47b3fc4f",
      "eventType": "AwsApiCall",
      "recipientAccountId": "527579490183"
      }""")

    assert result.region == "us-west-2"
    assert result.instanceId == "i-0f94de47f90462018"
    assert result.imageId == "ami-0ce21b51cb31a48b8"
    assert result.accountId == "527579490183"


def test_copy_ami():

    result = parse("""{
        "eventVersion": "1.05",
        "eventTime": "2020-04-01T04:06:48Z",
        "eventSource": "ec2.amazonaws.com",
        "eventName": "CopyImage",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "205.251.233.178",
        "userAgent": "console.ec2.amazonaws.com",
        "requestParameters": {
          "sourceRegion": "us-west-2",
          "sourceImageId": "ami-0528b3966f95526ee"
        },
        "responseElements": {
          "requestId": "3df999ff-e62b-4306-bd08-871b3f8c27e0",
          "imageId": "ami-00339be3aeeb7ac2d"
        },
        "requestID": "3df999ff-e62b-4306-bd08-871b3f8c27e0",
        "eventID": "3cf5b242-86b1-4b5b-9a4f-a2da69ab8c4c",
        "eventType": "AwsApiCall",
        "recipientAccountId": "527579490183"
      }""")

    assert result.region == "us-west-2"
    assert result.sourceImageId == "ami-0528b3966f95526ee"
    assert result.destinationImageId == "ami-00339be3aeeb7ac2d"
    assert result.accountId == "527579490183"


def test_ami_from_instance():

    result = parse("""{
        "eventVersion": "1.05",
        "eventTime": "2020-04-01T03:25:13Z",
        "eventSource": "ec2.amazonaws.com",
        "eventName": "CreateImage",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "205.251.233.178",
        "userAgent": "console.ec2.amazonaws.com",
        "requestParameters": {
          "instanceId": "i-0ed7c37bce75f98f9"
        },
        "responseElements": {
          "requestId": "e7999feb-6f64-4fc7-8507-17c5fbe8da29",
          "imageId": "ami-0528b3966f95526ee"
        },
        "requestID": "e7999feb-6f64-4fc7-8507-17c5fbe8da29",
        "eventID": "eeb6529b-8b20-41ea-983a-ef544830e81a",
        "eventType": "AwsApiCall",
        "recipientAccountId": "527579490183"
      }""")

    assert result.region == "us-west-2"
    assert result.instanceId == "i-0ed7c37bce75f98f9"
    assert result.destinationImageId == "ami-0528b3966f95526ee"
    assert result.accountId == "527579490183"
