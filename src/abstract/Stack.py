from typing import Generic, TypeVar

T = TypeVar("T")

class Pile(Generic[T]):
    _items: list[T] = []

    def __init__(self, item_set: list[T] = ()):
        # La pile est implémentée de gauche à droite. C'est-à-dire que le dernier élément ajouté est le dernier élément de la liste.
        self._items = list(item_set)[:]

    @property
    def sommet(self) -> T:
        if not len(self._items):
            return None

        return self._items[-1]

    @property
    def vide(self) -> bool:
        return len(self._items) == 0

    @property
    def taille(self) -> int:
        return len(self._items)

    @property
    def items(self) -> list[T]:
        return self._items[:]

    def empiler(self, item: T):
        self._items.append(item)
        return self

    def depiler(self) -> T:
        if not len(self._items):
            return None

        return self._items.pop()

    def clone(self):
        return Pile(self._items)

    def __str__(self):
        return f"Pile ({self.taille} éléments) { '✅' if not self.vide else '❌' }"

    def __repr__(self):
        return str(self)

    def __eq__(self, autre):
        if self.taille != autre.taille:
            return False

        for i in range(self.taille):
            if self.items[i] != autre.items[i]:
                return False
        return True

    def __cmp__(self, autre):
        return self.taille - autre.taille