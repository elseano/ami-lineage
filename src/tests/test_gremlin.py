from lineage.graph import LinkNodes
from lineage.gremlin import execute


class Stub:
    def __init__(self):
        self._calls = []

    def V(self):
        self._calls.append("V()")
        return self

    def addE(self, label, id1, id2):
        self._calls.append(
            """addE("{}", "{}", "{}")""".format(label, id1, id2))
        return self

    def addV(self, label):
        self._calls.append("""addV("{}")""".format(label))
        return self

    def property(self, k, v):
        self._calls.append("""property("{}", "{}")""".format(k, v))
        return self

    def to_string(self):
        return ".".join(self._calls)


def test_link_nodes():
    stub = Stub()
    execute(stub, LinkNodes("Thing", "1", "2"))
    assert """V().addE("Thing", "1", "2")""" == stub.to_string()
