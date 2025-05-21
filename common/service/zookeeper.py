from broker.BrokerService import BrokerService


class Zookeeper:

    def __init__(self):
        self.partition_broker_map = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2}
        self.broker_map = {1: BrokerService(1), 2: BrokerService(2)}

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

    def add_broker(self):
        """
        Adds a broker to Zookeeper.
        """
        # Logic to add a broker to Zookeeper
        pass

    def add_partition_to_broker(self, partition_id, broker_id):
        """
        Adds a partition to a broker in Zookeeper.
        """
        # Logic to add a partition to a broker in Zookeeper
        pass

    def remove_broker(self, broker_id):
        """
        Removes a broker from Zookeeper.
        """
        # Logic to remove a broker from Zookeeper
        pass

    def remove_partition_to_broker(self, partition_id, broker_id):
        """
        Removes a partition from a broker in Zookeeper.
        """
        # Logic to remove a partition from a broker in Zookeeper
        pass