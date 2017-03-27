# SVL 16-17 - M. Nebut
# CTD property-based testing
# ex d'utilisation d'Hypothesing, le code est tiré de
# https://hypothesis.readthedocs.io/en/master/stateful.html
# Il faudrait prendre le temps de rajouter de vraies classes
# Leaf et Split, tel quel c'est vraiment affreux.

# peut se lancer avec
# python3 tree.py

import unittest
from collections import namedtuple

from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule


Leaf = namedtuple('Leaf', ('label',))
Split = namedtuple('Split', ('left', 'right'))


class BalancedTrees(RuleBasedStateMachine):
    trees = Bundle('BinaryTree')

    @rule(target=trees, x=st.integers())
    def leaf(self, x):
        return Leaf(x)

    @rule(target=trees, left=trees, right=trees)
    def split(self, left, right):
        return Split(left, right)

    @rule(tree=trees)
    def check_balanced(self, tree):
        if isinstance(tree, Leaf):
            return
        else:
            assert abs(self.size(tree.left) - self.size(tree.right)) <= 1
            self.check_balanced(tree.left)
            self.check_balanced(tree.right)

    def size(self, tree):
        if isinstance(tree, Leaf):
            return 1
        else:
            return 1 + self.size(tree.left) + self.size(tree.right)

TestTrees = BalancedTrees.TestCase

if __name__ == '__main__':
    unittest.main()
