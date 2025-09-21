from collections import deque


class Packet:
    def __init__(self, source, destination, timestamp):
        self.source = source
        self.destination = destination
        self.timestamp = timestamp

    def tuple(self):
        return (self.source, self.destination, self.timestamp)

    def to_list(self):
        return list(self.tuple())

    def __hash__(self):
        return self.tuple().__hash__()

    def __eq__(self, other):
        return self.tuple().__eq__(other.tuple())


class PacketDeque:
    def __init__(self, destination):
        self.destination = destination
        self.buffer: list[Packet] = []
        self.ptr_left = 0
        self.ptr_right = 0  # exclusive

    def get_size(self):
        return self.ptr_right - self.ptr_left

    def push(self, packet: Packet):
        self.buffer.append(packet)
        self.ptr_right += 1

    def popleft(self):
        if self.get_size() == 0:
            raise Exception("empty queue")

        val = self.buffer[self.ptr_left]
        self.ptr_left += 1
        return val

    def get_count_within_time(self, starting_time, end_time):
        # get starting time tightest
        buf = self.buffer  # readability
        index_smallest = None
        index_largest = None

        left, right = self.ptr_left, self.ptr_right - 1
        while left <= right:
            mid = (left + right) // 2
            if starting_time <= buf[mid].timestamp:
                right = mid - 1
                index_smallest = mid
            else:
                left = mid + 1

        if index_smallest is None:
            return 0

        left, right = self.ptr_left, self.ptr_right - 1
        while left <= right:
            mid = (left + right) // 2
            if buf[mid].timestamp <= end_time:
                left = mid + 1
                index_largest = mid
            else:
                right = mid - 1

        if index_largest is None:
            return 0

        return index_largest - index_smallest + 1


class Router:
    def __init__(self, memoryLimit: int):
        self.packet_deque = deque()
        self.current_packets = set()
        self.destination_to_packet_deque = {}
        self.memory_limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        new_packet = Packet(source, destination, timestamp)
        if new_packet in self.current_packets:
            return False
        self.current_packets.add(new_packet)
        self.packet_deque.append(new_packet)
        self._add_to_destination_queue(new_packet, destination)

        if len(self.packet_deque) > self.memory_limit:
            self.forwardPacket()

        return True

    def _add_to_destination_queue(self, new_packet, destination):
        if destination not in self.destination_to_packet_deque.keys():
            self.destination_to_packet_deque[destination] = PacketDeque(destination)
        self.destination_to_packet_deque[destination].push(new_packet)

    def forwardPacket(self) -> List[int]:
        if not self.packet_deque:
            return []
        packet = self.packet_deque.popleft()
        self.current_packets.remove(packet)

        destination = packet.destination
        self.destination_to_packet_deque[destination].popleft()
        return packet.to_list()

    def _get_timestamp(self, packet):
        return packet[2]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destination_to_packet_deque.keys():
            return 0

        packet_deque = self.destination_to_packet_deque[destination]
        return packet_deque.get_count_within_time(startTime, endTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
