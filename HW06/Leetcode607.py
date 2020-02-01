class TwoSum:
    def __init__(self):
        self.dict1 = {}

    """
    @param: number: An integer
    @return: nothing
    """

    def add(self, number):
        # write your code here
        if number not in self.dict1:
            self.dict1[number] = 1
        else:
            self.dict1[number] += 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, target):
        # write your code here
        for key in self.dict1:
            compliment = target - key
            if compliment != key and compliment in self.dict1:
                return True
            elif compliment == key and compliment in self.dict1:
                return self.dict1[compliment] > 1

        return False