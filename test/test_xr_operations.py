from topology.topo_mgr.topo_mgr import Topology
from logger.cafylog import CafyLog

log = CafyLog("Test Topology")

class Test:
    topo = Topology(CafyLog.topology_file)


class TestTopology:
    def test_connect(self,):
        Test.device = Test.topo.get_device("R1")
        Test.device.connect()
        Test.peer =  Test.topo.get_device("R2")
        Test.peer.connect()

    def test_execute(self,):
        Test.device.execute("show version")
        Test.device.execute("show lldp neighbors")

    def test_config(self,):
        config = """
        interface Bundle-Ether738
            no shut
        """
        Test.device.config(config)
        Test.device.config("lldp")

    def test_parse(self,):
        Test.peer.config("lldp")
        Test.device.verify("show lldp neighbors",parse_only=True)

    def test_disconnect(self):
        Test.device.disconnect()
        Test.peer.disconnect()



