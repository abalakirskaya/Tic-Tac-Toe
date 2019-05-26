import sys
import random
import copy
from btnode import BSTNode
from btree import LinkedBST


sys.setrecursionlimit(100000)




class Board:


    computer_symbol = 'X'
    user_symbol = 'O'

    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.last_position = [None, None]
        self.last_symbol = None

    def last_symbol(self):
        return self.last_symbol



    def put_symbol(self, position, symbol):
        if position[0] < 0 or position[0] > 2 or position[1] < 0 or position[1] > 2:
            raise ValueError('Please, enter right position!')
        elif self.board[position[0]][position[1]] is not None:
            raise ValueError('The position ia already filled!')
        else:
            self.board[position[0]][position[1]] = symbol


    def build_tree(self, board):


        tree = LinkedBST()
        tree.add(board)
        computer_turn = False
        try:
            if self.last_symbol() == Board.user_symbol or Board.last_symbol() is None:
                computer_turn = True
        except:
            pass

        def recurse(node, computer_turn):
            try:
                free = bool(max([position is None for line in node.data for position in line]))
                if not free:
                    return None
            except:
                pass

            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if node.data[position[0]][position[1]] is None:
                    break
                else:
                    continue

            if Board.check_the_status(node.data) is not None:
                return None

            our_board = copy.deepcopy(node.data)
            if computer_turn:
                our_board[position[0]][position[1]] = Board.computer_symbol
            else:
                our_board[position[0]][position[1]] = Board.user_symbol

            node.left = BSTNode(our_board)

            while True:
                position = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
                if node.data[position[0]][position[1]] is None:
                    break
                else:
                    continue

            if Board.check_the_status(node.data) is not None:
                return None

            our_board = copy.deepcopy(node.data)
            if computer_turn:
                our_board[position[0]][position[1]] = Board.computer_symbol
            else:
                our_board[position[0]][position[1]] = Board.user_symbol

            node.right = BSTNode(our_board)

            if computer_turn is True:
                computer_turn = False
            elif computer_turn is False:
                computer_turn = True

            recurse(node.left, computer_turn)
            recurse(node.right, computer_turn)

        recurse(tree._root, computer_turn)
        return tree

    def choose_the_position(self):
        tree = self.build_tree(self.board)

        def counter(node):
            if node is not None:
                if node.left is None and node.right is None:
                    if Board.user_symbol == Board.check_the_status(node.data):
                        return -1
                    elif Board.computer_symbol == Board.check_the_status(node.data):
                        return 1
                    else:
                        return 0
                return (counter(node.left) + counter(node.right))
            else:
                pass
        left_counter = counter(tree._root.left)
        right_counter = counter(tree._root.right)
        try:
            if left_counter > right_counter:
                return tree._root.left.data
            else:
                return tree._root.left.data
        except:
            pass

    def __str__(self):
        """
        String representation of board
        :return str:
        """
        result = ""
        for line in self.board:
            for i in line:
                if i is None:
                    result += " "
                else:
                    result += i + " "
            result += "\n"

        return result



    @staticmethod
    def check_the_status(board):
        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return [i][0]

            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] and board[2][2] is not None:
            return board[2][2]

        if board[2][0] == board[1][1] == board[0][2] and board[0][2] is not None:
            return board[0][2]


    def free_position(self):
        free = bool(max([position is None for line in self.board for position in line]))
        return free
