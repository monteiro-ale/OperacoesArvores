from BinarySearchTree import BinarySearchTree

## Test

n = BinarySearchTree()
n.insert(8)
n.insert(3)
n.insert(1)
n.insert(6)
n.insert(4)
n.insert(7)
n.insert(10)
n.insert(14)
n.insert(13)
print('\n')
n.delete(4)
n.delete(7)
n.delete(10)
n.delete(14)
n.delete(13)
# print(n.search(84))
n.show(n.getRoot())
print('\n')