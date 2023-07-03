class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self._sequence = sequence
        self._start_index = start_index
        self._end_index = end_index
        self._current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index <= self._end_index:
            value = self._sequence[self._current_index]
            self._current_index += 1
            return value
        else:
            raise StopIteration


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterator = CustomIterator(sequence, 2, 7)

for value in iterator:
    print(value)
