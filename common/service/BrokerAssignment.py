from broker.BrokerService import BrokerService
from common.service.zookeeper import Zookeeper

class BrokerAssignment:

    def __init__(self, zookeeper: Zookeeper):
        self.zookeeper = zookeeper

    def fetch_broker(self, partition_id):
        broker_id = self.zookeeper.get_broker_for_partition(partition_id=partition_id)

        broker = self.zookeeper.get_broker_for_broker_id(broker_id=broker_id)

        """
        Fetches the broker for a given message.
        """
        return broker
    pass