from topology.topo_mgr.topo_mgr import Topology
from logger.cafylog import CafyLog

log = CafyLog("Test Topology")

class Test:
    topo = Topology(CafyLog.topology_file)


class TestTopology:
    def test_connect(self,):
        """
        Connect to testbeds

        :return:
        """
        Test.device = Test.topo.get_device("R1")
        Test.device.connect()
        Test.peer =  Test.topo.get_device("R2")
        Test.peer.connect()

    def test_execute(self,):
        """
        Execute some sample commands on the testbed

        :return:
        """
        Test.device.execute("show version")
        Test.device.execute("show lldp neighbors")

    def test_config(self,):
        """
        Configure a simple bundle interface

        :return:
        """
        config = """
        interface Bundle-Ether738
            no shut
        """
        Test.device.config(config)
        Test.device.config("lldp")

    def test_parse(self,):
        """
        Configure lldp and Parse it

        :return:
        """
        Test.peer.config("lldp")
        Test.device.verify("show lldp neighbors",parse_only=True)

    def test_disconnect(self):
        """
        Disconnect from Device

        :return:
        """
        Test.device.disconnect()
        Test.peer.disconnect()



