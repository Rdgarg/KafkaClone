from broker.BrokerService import BrokerService


class Zookeeper:

    def __init__(self):
        self.partition_broker_map = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2}
        self.broker_map = {1: BrokerService(1), 2: BrokerService(2)}

    def register_partition(self, partition_id, broker_id):
        """
        Registers a partition with a broker in Zookeeper.
        """
        # Logic to register the partition with Zookeeper
        pass

    def get_broker_for_partition(self, partition_id):
        """
        Gets the broker for a given partition from Zookeeper.
        """
        # Logic to get the broker for the partition from Zookeeper
        return self.partition_broker_map.get(partition_id, None)

    def get_broker_for_broker_id(self, broker_id):
        """
        Gets the broker for a given broker_id from Zookeeper.
        """
        # Logic to get the broker for the broker_id from Zookeeper
        return self.broker_map.get(broker_id, None)

    def get_total_partitions_number(self):
        """
        Gets the total number of partitions from Zookeeper.
        """
        # Logic to get the total number of partitions from Zookeeper
        return len(self.partition_broker_map)