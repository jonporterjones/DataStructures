import random

import hash_map
import pytest


def test_hash_map():
    """Test HashMap by simply exercising the functions it exposes."""

    test_word_set = {"big", "yellow", "bird", "dog", "taxi",
                     "small", "fish", "bug", "fry",
                     "very", "happy", "sometimes", "sad"}

    word_phrase = ' '.join(random.choices(population=list(test_word_set), k=2))

    hash_map_test = hash_map.HashMap()

    hash_map_test.upsert(word_phrase)

    assert len(hash_map_test.map) > 0

    word_phrase_test = hash_map_test.get(word_phrase)

    assert word_phrase in word_phrase_test

    hash_map_test.remove(word_phrase)

    assert len(hash_map_test.map) == 0

def test_hash_map_load():
    """Test HasMap under a small load."""

    n = 200
    found = False

    test_word_set = {"big", "yellow", "bird", "dog", "taxi",
                     "small", "fish", "bug", "fry",
                     "very", "happy", "sometimes", "sad"}

    hash_map_test = hash_map.HashMap()    
    for i in range(0, n):

        word_phrase = ' '.join(random.choices(population=list(test_word_set), k=2))
        hash_map_test.upsert(word_phrase)

    for i in range(0, n):

        word_phrase = ' '.join(random.choices(population=list(test_word_set), k=2))
        hash_value = hash_map_test.get(word_phrase)

        if word_phrase in hash_value:
            found = True
            break

    assert found