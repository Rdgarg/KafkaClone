from broker.BrokerService import BrokerService
from common.service.BrokerAssignment import BrokerAssignment
from common.service.PartitionFetcher import PartitionFetcher


class Producer:

    def __init__(self):
        self.partition_fetcher = PartitionFetcher()
        self.broker_fetcher = BrokerAssignment()

    def publish_message(self, message) -> str:
        """
        Publishes a message to the broker.
        """
        partition_id = self.partition_fetcher.fetch_partition(message)
        broker = self.broker_fetcher.fetch_broker(partition_id)
        message_id = broker.process_message(partition_id, message)
        # Logic to publish the message to the broker
        return message_id
