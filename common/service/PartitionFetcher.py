from common.models.Message import Message
import hashlib

from common.service.zookeeper import Zookeeper


class PartitionFetcher:
    def __init__(self, zookeeper: Zookeeper):
        self.zookeeper = zookeeper

    def fetch_partition(self, message:Message):

        key = message.key
        hash = hashlib.md5(key.encode("utf-8")).hexdigest()
        total_partitions = self.zookeeper.get_total_partitions_number()
        partition_id = int(hash, 16) % total_partitions
        return partition_id