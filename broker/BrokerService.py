

class BrokerService:
    def process_message(self, partition_id, message):
        """
        Processes a message for a given partition.
        """
        raise NotImplementedError()