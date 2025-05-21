from common.service.zookeeper import Zookeeper


class KafkaController:

    def __init__(self, zookeeper):
        self.zookeeper = zookeeper
        self.broker_map = {}
        self.partition_broker_map = {}

    def add_broker(self):
        self.zookeeper.add_broker()

    def add_partition_to_broker(self, partition_id, broker_id):
        self.zookeeper.add_partition_to_broker(partition_id, broker_id)

    def remove_broker(self, broker_id):
        """
        Removes a broker from the cluster.
        """
        # Logic to remove a broker from the cluster
        self.zookeeper.remove_broker(broker_id)

    def remove_partition_to_broker(self, partition_id, broker_id):
        """
        Removes a partition from a broker in the cluster.
        """
        # Logic to remove a partition from a broker in the cluster
        self.zookeeper.remove_partition_to_broker(partition_id, broker_id)
