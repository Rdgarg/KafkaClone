import pytest
from unittest.mock import MagicMock, patch

from common.service.zookeeper import Zookeeper
from producer.Producer import Producer
from common.models.Message import Message
from common.service.zookeeper import  Zookeeper
from common.service.BrokerAssignment import BrokerAssignment
from common.service.PartitionFetcher import PartitionFetcher

@pytest.fixture
def sample_message():
    return Message(
        value="test",
        key="key1",
        timestamp=123456789,
        headers={"header1": "value1"}
    )

def test_publish_message_success(sample_message):
        mock_broker = MagicMock()
        mock_broker.process_message.return_value = "msg-id-123"
        # Set up mocks
        zookeeper = Zookeeper()
        broker_assignment = BrokerAssignment(zookeeper)
        partition_fetcher = PartitionFetcher(zookeeper)
        producer = Producer( broker_assignment, partition_fetcher)
        result = producer.publish_message(sample_message)

        zookeeper.get_broker_for_broker_id(1).process_message.assert_called_once_with(42, sample_message)
        assert result == "msg-id-123"