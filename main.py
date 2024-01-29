
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

        def insert(self, position, parentNode): 

            #insert node if not used already 

            if position not in parentNode.used_positions: 

                #add to used positions if using it 
                appended_used_positions = parentNode.used_positions.copy() 
                appended_used_positions[position] = True 

                #add to children of parent node 
                parentNode.children[position] = TrieNode(grid[position], position) 

                





    class Trie(): 

        def __init__(self, position): 

            self.root = TrieNode(position) 

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

            if board[i] not in ("/", "n"): 

                row += 1 

                i += 1 

                continue 

            coordinate = Coordinate(i, row) 

            grid[coordinate] = board[i].lower()

        # Loop through grid 
        max_length = len(board)

        counter = 0
        
        for key in grid: 

            trie = Trie(key) 

            insert_adjacent_squares(trie) 

            def insert_adjacent_squares(trieNode): 

                while counter<max_length: 

                    #top left 
                    top_left = (coordinate.x - 1, coordinate.y -1) 
                    if top_left in grid:
                        newNode = TrieNode()
                        trieNode.insert(grid[top_left]) 

                    #if word is found in trie then add to final solution 
                    if self.word in wordlist: 

                        answers.add(self.word) 
                    #top middle 
                    top_middle = (coordinate.x, coordinate.y -1) 
                    if top_middle in grid:

                        trieNode.insert(grid[top_middle]) 

                    #top right 
                    top_right = (coordinate.x + 1, coordinate.y -1) 
                    if top_right in grid:

                        trieNode.insert(grid[top_right]) 

                    #middle right 
                    middle_right = (coordinate.x + 1, coordinate.y ) 
                    if middle_right in grid:

                        trieNode.insert(grid[middle_right]) 

                    #bottom right 
                    bottom_right = (coordinate.x + 1, coordinate.y + 1) 
                    if bottom_right in grid:

                        trieNode.insert(grid[bottom_right]) 

                    #bottom middle 
                    bottom_middle = (coordinate.x, coordinate.y + 1) 
                    if bottom_middle in grid:
                        trieNode.insert(grid[bottom_middle]) 

                    #bottom left 
                    bottom_left = (coordinate.x - 1, coordinate.y + 1) 
                    if bottom_left in grid:
                        trieNode.insert(grid[bottom_left]) 


                    #middle left 
                    middle_left = (coordinate.x - 1, coordinate.y -1) 
                    if middle_left in grid:
                        trieNode.insert(grid[middle_left]) 
         
        return answers 
 
def main():
    wordlist = ["eat", "art"]
    wordFinder = WordFinder(wordlist)
    
    board = "EATE\nLXRR\nARTR\nITSE\n"

    wordFinder.find_words(board)

if __name__ == "__main__":
    main()
from ast import List, Set
 