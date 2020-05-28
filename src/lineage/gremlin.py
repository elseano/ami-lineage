import collections

from gremlin_python.process.graph_traversal import __
from gremlin_python.process.traversal import T

CreateNode = collections.namedtuple("CreateNode", ["label", "id"])
EnsureNode = collections.namedtuple("EnsureName", ["label", "id"])
LinkNodes = collections.namedtuple("LinkNodes", ["label", "fromId", "toId"])


def to_gremlin(command):
    if type(command).__name__ == "CreateNode":
        return """g.V().addV("{}").property(T.id, "{}")"""

    if type(command).__name__ == "EnsureNodes":
        return None

    if type(command).__name__ == "LinkNodes":
        return """g.V().addE("{}", "{}", "{}")""".format(command.label, command.fromId, command.toId)


def execute(traversal, command):
    print(f"[Gremlin] Executing Command: {command}")

    if type(command).__name__ == "CreateNode":
        return traversal.V().addV(command.label).property(T.id, command.id)
    if type(command).__name__ == "LinkNodes":
        return traversal.V().addE(command.label, command.fromId, command.toId)


def execute_all(traversal, commands):
    for cmd in commands:
        execute(traversal, cmd)
