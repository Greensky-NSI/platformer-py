class Cache:
    _cache = {}  # Dictionnaire pour stocker les données en cache

    def __init__(self):
        self._cache = {}  # Initialisation du cache vide lors de la création d'une instance de la classe

    def cache(self, key, value = None):
        """
        Stocke une valeur dans le cache ou récupère le cache complet si aucune valeur n'est spécifiée.

        :param key: any - Clé pour stocker la valeur dans le cache.
        :param value: any, optionel -  Valeur à stocker dans le cache. Si aucune valeur n'est spécifiée, renvoie le cache complet.

        :return any - La valeur stockée dans le cache ou le cache complet.
        """
        if value is None:
            if key in self._cache:
                self._cache.pop(key)  # Supprime la valeur du cache si elle existe
            return self._cache  # Renvoie le cache complet

        self._cache[key] = value  # Stocke la valeur dans le cache
        return value  # Renvoie la valeur stockée

    def delete(self, key):
        """
        Supprime une valeur du cache en utilisant la clé spécifiée.

        :param key: any - Clé pour supprimer la valeur du cache.
        """
        if key in self._cache:
            self._cache.pop(key)  # Supprime la valeur du cache si elle existe

    def get(self, key, default = None):
        """
        Récupère une valeur du cache en utilisant la clé spécifiée.

        :param key: any - Clé pour récupérer la valeur du cache.
        :param default: any, optional -  Valeur par défaut à renvoyer si la clé n'existe pas dans le cache.

        :return: any - La valeur correspondante à la clé dans le cache, ou la valeur par défaut si la clé n'existe pas.
        """
        return self._cache.get(key, default)  # Renvoie la valeur correspondante à la clé dans le cache, ou la valeur par défaut si la clé n'existe pas.