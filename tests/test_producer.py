import pytest
from unittest.mock import MagicMock, patch
from producer.Producer import Producer
from common.models.Message import Message

@pytest.fixture
def sample_message():
    return Message(
        value="test",
        key="key1",
        timestamp=123456789,
        headers={"header1": "value1"}
    )

def test_publish_message_success(sample_message):
    with patch("producer.Producer.PartitionFetcher") as MockPartitionFetcher, \
         patch("producer.Producer.BrokerAssignment") as MockBrokerAssignment:

        # Set up mocks
        mock_partition_fetcher = MockPartitionFetcher.return_value
        mock_broker_fetcher = MockBrokerAssignment.return_value
        mock_partition_fetcher.fetch_partition.return_value = 42
        mock_broker = MagicMock()
        mock_broker_fetcher.fetch_broker.return_value = mock_broker
        mock_broker.process_message.return_value = "msg-id-123"

        producer = Producer()
        result = producer.publish_message(sample_message)

        mock_partition_fetcher.fetch_partition.assert_called_once_with(sample_message)
        mock_broker_fetcher.fetch_broker.assert_called_once_with(42)
        mock_broker.process_message.assert_called_once_with(42, sample_message)
        assert result == "msg-id-123"