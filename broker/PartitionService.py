

class PartitionService:
    def __init__(self, broker, partition_id):
        self.broker = broker
        self.partition_id = partition_id

    def create_partition(self, topic):
        if topic not in self.partitions:
            self.partitions[topic] = []
            self.partition_count += 1
            return True
        return False

    def get_partitions(self, topic):
        return self.partitions.get(topic, [])