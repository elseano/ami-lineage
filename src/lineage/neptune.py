from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

graph = Graph()

remoteConn = DriverRemoteConnection(
    'wss://lineage.cktjgcfqinwz.us-west-2.neptune.amazonaws.com:8182/gremlin', 'g')
traversal = graph.traversal().withRemote(remoteConn)
