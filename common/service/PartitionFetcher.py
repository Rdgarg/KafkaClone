from common.models.Message import Message


class PartitionFetcher:
    def fetch_partition(self, message:Message):
        """
        Fetches the partition for a given message.
        """
        raise NotImplementedError()