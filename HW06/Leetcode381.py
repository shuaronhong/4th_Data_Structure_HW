class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.idx = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.elements.append(val)
        self.idx[val].add(len(self.elements) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False
        last = self.elements[-1]
        to_remove = self.idx[val].pop()
        self.elements[to_remove] = last
        self.idx[last].add(to_remove)
        self.idx[last].discard(len(self.elements) - 1)

        self.elements.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.elements)