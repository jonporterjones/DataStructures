"""
Demonstrate a simple hash map.

The hash map is stored as a dictionary in the HashMap class.
The dictionary keys are the numeric representations of the hash.
The values are the set of phrases that map to that hash.
This accounts for the unlikely possibility of a hash collision.
"""

import hashlib
from typing import Set


class HashMap():
    """Map phrases to a hash.  For each phrase, store the number of occurrences."""

    def __init__(self) -> None:
        """
        Initialize hash map with an empty dictionary.
        """
        self.map = {}

    def _compute_hash(self, phrase: str) -> int:
        return int.from_bytes(hashlib.md5(phrase.encode('utf-8')).digest(), byteorder='big')

    def upsert(self, phrase: str):
        """Upsert a new hash.

        Args:
            phrase (str): The phrase to be hashed.
        """
        hash = self._compute_hash(phrase)
        hashed_value: Set = self.map.get(hash, set())
        hashed_value.add(phrase)
        self.map[hash] = hashed_value

    def get(self, phrase: str) -> Set:
        """Return hashed value for supplied phrase.

        Args:
            phrase (str): The phrase.

        Returns:
            Set: The set of values hashed for the phrase.
        """
        hash = self._compute_hash(phrase)

        return self.map.get(hash, set())

    def remove(self, phrase: str):
        """
        Remove a phrase from the hashed value, if it exists.

        Args:
            phrase (str): The phrase to check.
        """
        hash = self._compute_hash(phrase)
        hashed_value: Set = self.map.get(hash, set())

        # If phrase is hashed and there is only 1 value, remove key from dictionary.
        # If phrase is hashed and there are multiple values, remove phrase from hash.
        if hashed_value:
            if len(hashed_value) == 1:
                _ = self.map.pop(hash, {})
            else:
                hashed_value = hashed_value.discard(phrase)
                self.map[hash] = hashed_value
