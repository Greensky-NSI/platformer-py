class Pile:
    _items = []

    def __init__(self, item_set: list = []):
        # La pile est implémentée de gauche à droite. C'est-à-dire que le dernier élément ajouté est le dernier élément de la liste.
        self._items = item_set[:]

    @property
    def sommet(self):
        if not len(self._items):
            return None

        return self._items[-1]

    @property
    def vide(self):
        return len(self._items) == 0

    @property
    def taille(self):
        return len(self._items)

    @property
    def items(self):
        return self._items

    def empiler(self, item):
        self._items.append(item)

    def depiler(self):
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