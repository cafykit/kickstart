from topology.topo_mgr.topo_mgr import Topology
from logger.cafylog import CafyLog

log = CafyLog("Test Topology")

class Test:
    topo = Topology(CafyLog.topology_file)


class TestTopology:
    def test_get_devices(self,):
        """
        Get the list of device on topology


        :return:
        """
        Test.devices = Test.topo.get_devices()
        log.info(Test.devices)


    def test_get_device(self):
        """
        Get a device from topology

        :return:
        """
        Test.device = Test.topo.get_device("R1")
        log.info(Test.device.name)
        log.info(Test.device.alias)


    def test_get_interfaces(self):
        """
        Get interfaces from topology

        :return:
        """
        interfaces = Test.device.get_interfaces()
        log.info(interfaces)


    def test_get_interfaces_peer(self):
        """
        Get interfaces from topology for a given peer

        :return:
        """
        Test.peer = Test.topo.get_router("R2")
        interfaces = Test.device.get_interfaces(peer=Test.peer)
        log.info(interfaces)


    def test_get_links(self):
        """
        Get links from topology

        :return:
        """
        links = Test.device.get_links()
        log.info(links)


    def test_get_handle(self):
        """
        Get handles from topology

        :return:
        """
        cli_handle = Test.device.get_cli_handle()
        log.info(cli_handle)

        console_handle = Test.device.get_handle("console")
        log.info(console_handle)



