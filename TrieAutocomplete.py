# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.
class TrieNode():
    def __init__(self):

        # Initialising one node for trie
        self.children = {}
        self.end = False

class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()
        self.word_list = []

    def CREATE_TRIE_FOR_ALL_KEYS(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.INSERT_WORD_INTO_TRIE(key) # inserting one key to the trie.

    def INSERT_WORD_INTO_TRIE(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root
        #print("list :",list(key))
        for a in list(key):
            if a not in node.children:
                #if this character not in node.children then insert it to node's children
                node.children[a] = TrieNode()
            # go to the node that you  recently inserted because all characters are yet to be inserted
            node = node.children[a]

        node.end = True


    def SEARCH(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        for a in list(key):
            if not node.children[a]:
                found = False
                break

            node = node.children[a]
        return node and node.end and found

    def ExploreTheChildren(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.end:
            self.word_list.append(word)

        for character, nextnode in node.children.items():
            self.ExploreTheChildren(nextnode, word + character)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common prefix is the given KEY thus listing out all
        # the suggestions for autocomplete.

        node = self.root
        not_found = False

        for a in list(key):
            if a not in node.children:
                not_found = True
                break
            # go to the node that you recently visited because all characters are yet to be visited of given prefix key
            node = node.children[a]

        if not_found:
            # THIS KEY WITH PREFIX DOESN'T EXISTS
            return 0
        elif node.end and not node.children:
            # THE KEY IS WORD PRESENT IN TRIE WITH NO FURTHER CHILDREN
            return -1

        # THIS KEY MAY BE RESENT AS WORD IN TRIE WITH FURTHER CHILDREN OR
        # THIS PREFIX FOUND IN TRIE
        # node : is a node till which you found the prefix
        self.ExploreTheChildren(node, key)

        for s in self.word_list:
            print(s)
        return 1

# Driver Code
keys = ["hello", "dog", "hell", "cat", "a",
        "hel", "help", "helps", "helping","catalyst","cataclysm"] # keys to form the trie structure.
key = "ca" # key for autocomplete suggestions.
status = ["Not found", "Found"]

# creating trie object
T = Trie()

# creating the trie structure with the
# given set of strings.
T.CREATE_TRIE_FOR_ALL_KEYS(keys)

# autocompleting the given key using
# our trie structure.
comp = T.printAutoSuggestions(key)

if comp == -1:
    print("THIS STRING IS PRESENT BUT No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")

    # This code is contributed by amurdia