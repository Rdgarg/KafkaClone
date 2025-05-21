from broker.BrokerService import BrokerService
from common.models.Message import Message
from common.service.BrokerAssignment import BrokerAssignment
from common.service.PartitionFetcher import PartitionFetcher


class Producer():
    def __init__(self, broker_assignment: BrokerAssignment, partition_fetcher: PartitionFetcher):
        self.broker_assignment = broker_assignment
        self.partition_fetcher = partition_fetcher

    def publish_message(self, message:Message) -> str:
        """
        Publishes a message to the broker.
        """
        partition_id = self.partition_fetcher.fetch_partition(message)
        broker = self.broker_assignment.fetch_broker(partition_id)
        message_id = broker.process_message(partition_id, message)
        # Logic to publish the message to the broker
        return message_id

    def validate_message(self,message:Message):
        if not message:
            raise ValueError("Message cannot be None")
        if message.value is None:
            raise ValueError("Message value cannot be None")
        return
