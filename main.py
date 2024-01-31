from typing import List, Set


class WordFinder:
    class Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class TrieNode:
        def __init__(self, letter, position):
            self.word = position
            self.word += letter
            self.children = {}
            self.used_positions = {}
            self.is_word = False

        def insert(self, letter, position, parentNode) -> str:
            # insert node if not used already

            if position not in parentNode.used_positions:
                # add to used positions if using it
                appended_used_positions = parentNode.used_positions.copy()
                appended_used_positions[position] = True

                # Create new node and add to children of parent node
                parentNode.children[position] = WordFinder.TrieNode(letter, position)

            return parentNode.children[position].word

    class Trie:
        def __init__(self, letter, position):
            self.root = WordFinder.TrieNode(letter, position)

    def __init__(self, wordlist: List[str]):
        self.wordlist = wordlist

    def find_words(self, board: str) -> Set[str]:
        print("Hello world!")
        board = "EATE\nLXRR\nARTR\nITSE\n"
        answers = set(())

        # Convert string into grid dictionary
        grid = {}
        row = 0

        for i in range(len(board)):
            if board[i] == ("/"):
                row += 1
                i += 1
                continue
            coordinate = WordFinder.Coordinate(i, row)
            grid[coordinate] = board[i].lower()

        # Loop through grid
        max_length = len(board)
        counter = 0

        for key in grid:
            trie = WordFinder.Trie(grid[key], key)
            insert_adjacent_squares(trie)

        def insert_adjacent_squares(trieNode):
            while counter < max_length:
                directions = [
                    (-1, -1),
                    (0, -1),
                    (1, -1),  # top left, top middle, top right
                    (1, 0),  # middle right
                    (1, 1),
                    (0, 1),
                    (-1, 1),  # bottom right, bottom middle, bottom left
                    (-1, 0),  # middle left
                ]

                for direction in directions:
                    new_x, new_y = (
                        coordinate.x + direction[0],
                        coordinate.y + direction[1],
                    )
                    new_coordinate = WordFinder.Coordinate(new_x, new_y)

                    # check if coordinate is in grid and coordinate contains a letter
                    if new_coordinate in grid and grid[new_coordinate] != " ":
                        letter = grid[new_coordinate]
                        #creates new node
                        new_node_word = trieNode.insert(
                            letter, new_coordinate, trieNode
                        )
        
        counter += 1
        
        def search_using_wordlist():
            #to implement
            print("search")
def main():
    wordlist = ["eat", "art"]
    wordFinder = WordFinder(wordlist)

    board = "EATE\nLXRR\nARTR\nITSE\n"

    for word in wordFinder.find_words(board):
        print(word)


if __name__ == "__main__":
    main()
from ast import List, Set
