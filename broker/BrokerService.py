

class BrokerService:

    def __init__(self, broker_id):
        self.broker_id = broker_id
        self.partition_list = []


    def process_message(self, partition_id, message):
        """
        Processes a message for a given partition.
        """
        raise NotImplementedError()