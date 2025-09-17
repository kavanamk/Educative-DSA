from trie_node import *

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, data):
        node = self.root
        for char in data:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.search_words) < 3:
                node.search_words.append(data)

    def search(self, word):
        result, node = [], self.root
        for i, char in enumerate(word):
            if char not in node.children:
                temp = [[] for _ in range(len(word) - i)]
                return result + temp
            else:
                node = node.children[char]
                result.append(node.search_words[:])
        return result


def suggested_products(products, search_word):
    products.sort()
    trie = Trie()
    for x in products:
        trie.insert(x)
    return trie.search(search_word)


# Driver code
def main():
    products = ["bat", "bag", "bassinet", "bread", "cable",
                "table", "tree", "tarp"]
    search_word_list = ["ba", "in", "ca", "t"]
    for i in range(len(search_word_list)):
        print(i + 1, ".\tProducts:", products, sep="")
        print("\tSearch keyword: '", search_word_list[i], "'", sep="")
        print("\tSuggested Products: ", suggested_products(
            products, search_word_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
