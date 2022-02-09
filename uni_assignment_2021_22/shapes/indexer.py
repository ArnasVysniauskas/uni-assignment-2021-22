class Indexer:
    _last_index: int = 0
    _free_indeces: list[int] = []

    def get_new_index(self) -> int:
        new_index: int

        if len(self._free_indeces) == 0:
            new_index = self._last_index
            self._last_index += 1
        else:
            new_index = self._free_indeces.pop()

        return new_index

    def remove_index(self, index: int) -> None:
        if index == self._last_index - 1:
            self._normalise_last_index()
        else:
            self._free_indeces.append(index)

    def _normalise_last_index(self):
        if self._last_index - 1 in self._free_indeces:
            self._last_index -= 1
            self._free_indeces.remove(self._last_index)
