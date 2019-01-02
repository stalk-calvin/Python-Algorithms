from calvin.data_structure.linkedlist import ListNode, LinkedList


class Node(object):
    """
    Implementation of a Node in a Binary Search Tree.
    """

    def __init__(self, key=None, val=None, size_of_subtree=1, left=None, right=None):
        self.key = key
        self.val = val
        self.size_of_subtree = size_of_subtree
        self.left = left
        self.right = right

class BinaryTree(object):
    def build_tree(self):
        root = Node(0, 1)
        root.left = Node(0,2)
        root.right = Node(0,3)
        return root

    def find_inorder_wrapper(self, root):
        result = []
        if root is None: return result
        return self.__find_inorder(root, result)

    def __find_inorder(self, root, result):
        if root is None: return result
        self.__find_inorder(root.left, result)
        result.append(root.val)
        self.__find_inorder(root.right, result)
        return result

    def serialize_preorder(self, root, out):
        if root == None:
            out.append('#')
        else:
            out.append(str(root.val))
            self.serialize_preorder(root.left, out)
            self.serialize_preorder(root.right, out)

    def serialize_inorder(self, root, out):
        if root == None:
            out.append('#')
        else:
            self.serialize_preorder(root.left, out)
            out.append(str(root.val))
            self.serialize_preorder(root.right, out)

    def serialize_postorder(self, root, out):
        if root == None:
            out.append('#')
        else:
            self.serialize_preorder(root.left, out)
            self.serialize_preorder(root.right, out)
            out.append(str(root.val))

    def deserialize_pretree(self, s):
        if not s:
            return None

        n=None
        value = s.popleft()
        if value != '#':
            n=Node(0, int(value))
            n.left = self.deserialize_pretree(s)
            n.right = self.deserialize_pretree(s)
        return n

    def first_common_ancestor(self, root, t1, t2):
        if root == None:
            return None
        if root is t1 or root is t2:
            return root
        left = self.first_common_ancestor(root.left, t1, t2)
        right = self.first_common_ancestor(root.right, t1, t2)
        if left and right:
            #found!
            return root
        if left == None:
            return right
        else:
            return left

    def check_subtree(self, t1, t2):
        if t2 == None:
            return True
        return self.__sub_tree(t1, t2)

    def __sub_tree(self, t1, t2):
        if t1 == None:
            return False
        elif t1.val == t2.val and self.__match_tree(t1, t2):
            return True
        return self.__sub_tree(t1.left, t2) or self.__sub_tree(t1.right, t2)

    def __match_tree(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        elif t1.val != t2.val:
            return False
        else:
            return self.__match_tree(t1.left, t2.left) and self.__match_tree(t1.right, t2.right)

    def path_sum(self, tree, to, current):
        if tree == None:
            return 0
        current += tree.val

        total_paths = 0
        if to == current:
            total_paths += 1

        total_paths += self.path_sum(tree.left, to, current)
        total_paths += self.path_sum(tree.right, to, current)

        return total_paths

    def path_sum_result(self, tree, to, current, result, line):
        if tree == None:
            return None

        current += tree.val
        line.append(tree.val)

        if to == current:
            result.append(line)

        self.path_sum_result(tree.left, to, current, result, list(line))
        self.path_sum_result(tree.right, to, current, result, list(line))

        return result


    def even_sum(self, tree):
        max=[0]
        self.__even_sum_helper(tree, max)
        return max[0]

    def __even_sum_helper(self, tree, max):
        if not tree:
            return

        if max[0]+tree.val % 2 == 0 and max[0] < max[0]+tree.val:
            max[0]=max[0]+tree.val

        self.__even_sum_helper(tree.left, max)
        self.__even_sum_helper(tree.right, max)


class BalancedWithHeight(object):
    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height

from collections import deque
class BinarySearchTree(object):
    """
    Implementation of a Binary Search Tree.
    """
    def __init__(self):
        self.root = None

    @staticmethod
    def __get_height(tree):
        if tree==None:
            return 0

        return max(BinarySearchTree.__get_height(tree.left), BinarySearchTree.__get_height(tree.right)) + 1

    def is_balanced_bf(self, tree):
        if tree==None:
            return True
        height = BinarySearchTree.__get_height(tree.left) + BinarySearchTree.__get_height(tree.right)
        if (height > 1):
            return False

        return self.is_balanced_bf(tree.left) and self.is_balanced_bf(tree.right)

    def is_balanced(self,tree):
        if tree==None:
            return BalancedWithHeight(True, -1)
        left = self.is_balanced(tree.left)
        if (not left.balanced):
            return left
        right = self.is_balanced(tree.right)
        if (not right.balanced):
            return right
        balanced = True
        if abs(left.height - right.height) > 1:
            balanced = False
        height = max(left.height, right.height) + 1
        return BalancedWithHeight(balanced, height)

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        """
        Return the number of nodes in the BST

        Worst Case Complexity: O(1)

        Balanced Tree Complexity: O(1)
        """
        return self._size(self.root)

    def is_empty(self):
        """
        Returns True if the BST is empty, False otherwise

        Worst Case Complexity: O(1)

        Balanced Tree Complexity: O(1)
        """
        return self.size() == 0

    def _get(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.val

    def get(self, key):
        """
        Return the value paired with 'key'

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        return self._get(key, self.root)

    def contains(self, key):
        """
        Returns True if the BST contains 'key', False otherwise

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        return self.get(key) is not None

    def _put(self, key, val, node):

        # If we hit the end of a branch, create a new node
        if node is None:
            return Node(key, val)

        # Follow left branch
        if key < node.key:
            node.left = self._put(key, val, node.left)
        # Follow right branch
        elif key > node.key:
            node.right = self._put(key, val, node.right)
        # Overwrite value
        else:
            node.val = val

        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def put(self, key, val):
        """
        Add a new key-value pair.

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        self.root = self._put(key, val, self.root)


    def _min_node(self):
        """
        Return the node with the minimum key in the BST
        """
        min_node = self.root
        # Return none if empty BST
        if min_node is None:
            return None

        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        """
        Return the minimum key in the BST

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        min_node = self._min_node()
        if min_node is None:
            return None
        else:
            return min_node.key

    def _max_node(self):
        """
        Return the node with the maximum key in the BST
        """
        max_node = self.root
        # Return none if empty BST
        if max_node is None:
            return None

        while max_node.right is not None:
            max_node = max_node.right

        return max_node

    def max_key(self):
        """
        Return the maximum key in the BST

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        max_node = self._max_node()
        if max_node is None:
            return None
        else:
            return max_node.key

    def _floor_node(self, key, node):
        """
        Returns the node with the biggest key that is less than or equal to the
        given value 'key'
        """
        if node is None:
            return None

        if key < node.key:
            # Floor must be in left subtree
            return self._floor_node(key, node.left)

        elif key > node.key:
            # Floor is either in right subtree or is this node
            attempt_in_right = self._floor_node(key, node.right)
            if attempt_in_right is None:
                return node
            else:
                return attempt_in_right

        else:
            # Keys are equal so floor is node with this key
            return node

    def floor_key(self, key):
        """
        Returns the biggest key that is less than or equal to the given value
        'key'

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        floor_node = self._floor_node(key, self.root)
        if floor_node is None:
            return None
        else:
            return floor_node.key

    def _ceiling_node(self, key, node):
        """
        Returns the node with the smallest key that is greater than or equal to
        the given value 'key'
        """
        if node is None:
            return None

        if key < node.key:
            # Ceiling is either in left subtree or is this node
            attempt_in_left = self._ceiling_node(key, node.left)
            if attempt_in_left is None:
                return node
            else:
                return attempt_in_left
        elif key > node.key:
            # Ceiling must be in right subtree
            return self._ceiling_node(key, node.right)
        else:
            # Keys are equal so ceiling is node with this key
            return node

    def ceiling_key(self, key):
        """
        Returns the smallest key that is greater than or equal to the given
        value 'key'

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        ceiling_node = self._ceiling_node(key, self.root)
        if ceiling_node is None:
            return None
        else:
            return ceiling_node.key

    def _select_node(self, rank, node):
        """
        Return the node with rank equal to 'rank'
        """
        if node is None:
            return None

        left_size = self._size(node.left)
        if left_size < rank:
            return self._select_node(rank - left_size - 1, node.right)
        elif left_size > rank:
            return self._select_node(rank, node.left)
        else:
            return node

    def select_key(self, rank):
        """
        Return the key with rank equal to 'rank'

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        select_node = self._select_node(rank, self.root)
        if select_node is None:
            return None
        else:
            return select_node.key

    def _rank(self, key, node):
        if node is None:
            return None

        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return self._size(node.left) + self._rank(key, node.right) + 1

        else:
            return self._size(node.left)

    def rank(self, key):
        """
        Return the number of keys less than a given 'key'.

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        return self._rank(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)

        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                old_node = node
                node = self._ceiling_node(key, node.right)
                node.right = self._delete_min(old_node.right)
                node.left = old_node.left
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete(self, key):
        """
        Remove the node with key equal to 'key'

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        self.root = self._delete(key, self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_min(self):
        """
        Remove the key-value pair with the smallest key.


        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        self.root = self._delete_min(self.root)

    def _delete_max(self, node):
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.size_of_subtree = self._size(node.left) + self._size(node.right)+1
        return node

    def delete_max(self):
        """
        Remove the key-value pair with the largest key.

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        """
        self.root = self._delete_max(self.root)

    def _keys(self, node, keys):
        if node is None:
            return keys

        if node.left is not None:
            keys = self._keys(node.left, keys)

        keys.append(node.key)

        if node.right is not None:
            keys = self._keys(node.right, keys)

        return keys

    def keys(self):
        """
        Return all of the keys in the BST in aschending order

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(N)
        """
        keys = []
        return self._keys(self.root, keys)

    def LCA(self, root, l, r):
        while (root != None):
            if (root.val < l and root.val < r):
                root = root.right
            elif (root.val > l and root.val > r):
                root = root.left
            else:
                return root
        return root


    def create_minimal_bst_tree(self, sorted_array, start, end):
        if end<start:
            return None

        m=int(start+(end-start)/2)
        root=Node(0, sorted_array[m])
        root.left = self.create_minimal_bst_tree(sorted_array, start, m-1)
        root.right = self.create_minimal_bst_tree(sorted_array, m+1, end)
        return root

    def bfs_with_level(self, root):
        result=[]
        if root==None:
            return None

        q = deque()
        q.append(root)
        level_node = Node(0, 0)
        q.append(level_node)
        level = 1
        while q:
            t=q.popleft()

            if (t is level_node):
                if not q:
                    break
                level += 1
                q.append(level_node)
                continue

            result.append(t.val)

            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)

        return (result, level)

    def level(self, root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            depthLeft = 1+self.level(root.left)
            depthRight = 1+self.level(root.right)
            if depthLeft > depthRight:
                return depthLeft
            else:
                return depthRight

    def list_of_depths(self, root):
        result=[]

        if root == None or root.left == None and root.right == None:
            result = [ListNode(root.val)]
            return result

        q=deque()
        q.append(root)
        current_ll=LinkedList()
        current_ll.append(root.val)
        tracker = LinkedList()
        tracker.append(root)
        while tracker.head:
            result.append(current_ll)
            parents=tracker.head
            tracker=LinkedList()
            current_ll=LinkedList()
            while parents:
                ll=parents.value
                if ll.left:
                    tracker.append(ll.left)
                    current_ll.append(ll.left.val)
                if ll.right:
                    tracker.append(ll.right)
                    current_ll.append(ll.right.val)
                parents = parents.next
        return result

    def is_bst(self, tree):
        if tree == None or (tree.left == None and tree.right == None):
            return True

        val = tree.val
        if (tree.left and tree.left.val > val) or (tree.right and tree.right.val < val):
            return False

        return self.is_bst(tree.left) and self.is_bst(tree.right)

    def first_common_ancestor(self, root, t1, t2):
        if root == None:
            return None
        if root.val > t1.val and root.val > t2.val:
            return self.first_common_ancestor(root.left, t1, t2)
        elif root.val < t1.val and root.val < t2.val:
            return self.first_common_ancestor(root.right, t1, t2)
        else:
            return root.val

    def flipEquiv(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        flag1 = (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
        flag2 = (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

        return flag1 or flag2

