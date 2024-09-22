class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            # add to array of timestamps
            self.store[key]['times'].append(timestamp)
            self.store[key][timestamp] = value
        else:
            self.store[key] = {
                "times": [timestamp]
            }
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # Key doesn't exist O(1)
        if key not in self.store:
            return ""

        # Exact timestamp exists O(1)
        if timestamp in self.store[key]:
            return self.store[key][timestamp]
        
        # Check for most recent timestamp O(log n)
        key_times = self.store[key]['times']
        l, r = 0, len(key_times)
        curr_time = None

        while l < r:
            m = (l + r) // 2

            if timestamp < key_times[m]:
                r = m
            elif timestamp > key_times[m]:
                curr_time = key_times[m]
                l = m + 1

        if curr_time:
            return self.store[key][curr_time]
        else:
            return ""