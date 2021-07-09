import nltk
from nltk import word_tokenize, pos_tag

# Create the hash table and the size of it
class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.bucket = [None] * self.capacity


# Make a separate chaining link to avoid collisions
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# avoid pile ups in the same bucket
def hash(self, key):
    hashsum = 0

    for idx, c in enumerate(key):
        hashsum += (idx + len(key)) ** ord(c)
        hashsum = hashsum % self.capacity
    return hashsum


# Insert key/value pair into hash table
def insert(self, key, value):
    self.size += 1
    index = self.hash(key)
    node = self.bucket[index]

    if node is None:
        self.buckets[index] = Node(key, value)
        return

    prev = node
    while node is not None:
        prev = node
        node = node.next
        prev.next = Node(key, value)


# Retrieve data in the hash table
def find(self, key):
    index = self.hash(key)
    node = self.buckets[index]

    while node is not None and node.key != key:
        node = node.next

    if node is None:
        return None
    else:
        return node.value


# Remove elements in a hash table
def remove(self, key):
    index = self.hash(key)
    node = self.buckets[index]
    prev = None

    while node is not None and node.key != key:
        prev = node
        node = node.next

    if node is None:
        return None
    else:
        self.size -= 1
        result = node.value

        if prev is None:
            node = None
        else:
            prev.next = prev.next.next

        return result


# text = "It was a quiet impressive essay regarding the content. It could have been more properly structured as there were fewer headings and bullets. Overall good work"
# list = pos_tag(word_tokenize(text))
# print()

