from src.abstract.Cache import Cache


class Ticker:
    _current_tick: int = 0
    _refs = Cache()

    def __init__(self):
        self._current_tick = 0

    def tick(self):
        self._current_tick += 1

    @property
    def current_tick(self):
        return self._current_tick

    def register(self, ref):
        self._refs.cache(ref, self._current_tick)

    def diff(self, ref):
        return self._current_tick - self._refs.get(ref, 0)
