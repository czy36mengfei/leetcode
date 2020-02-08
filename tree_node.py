# 二叉树的后序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_binary_tree(node_list):
    length = len(node_list)
    if length == 0:
        return None
    root = TreeNode(node_list[0])
    queue = [root]
    i = 1
    while i < length:
        node = queue.pop(0)
        if node_list[i]:
            left = TreeNode(node_list[i])
            node.left = left
            queue.append(left)
        i += 1

        if i < length:
            if node_list[i]:
                right = TreeNode(node_list[i])
                node.right = right
                queue.append(right)
            i+=1

    return root


def print_binary_tree(root):
    # bfs
    if not root:
        return
    layer_bound = TreeNode(-10000)
    queue = [root, layer_bound]
    res_str = ''
    res_str += str(root.val) + '\n'
    while queue:
        node = queue.pop(0)
        if node.val == -10000:
            res_str += '\n'
            if len(queue) == 0:
                break
            queue.append(layer_bound)
            continue
        # res_str += str(node.val)

        left = node.left
        right = node.right
        if left:
            # print(str(left.val) + ' |')
            queue.append(left)
            res_str += '(' + str(left.val) + ' '
        else:
            res_str += '( '
        if right:
            # print('| ' + str(right.val))
            queue.append(right)
            res_str += ' ' + str(right.val) + ')'
        else:
            res_str += ' )'
    return res_str


def node_list_input(node_list_str):
    node_list = [int(v) if v != 'null' else None for v in node_list_str]
    return node_list

if __name__ == '__main__':
    while True:
        node_list_str = input().strip().split()
        node_list = [int(v) if v != 'null' else None for v in node_list_str]

        res = get_binary_tree(node_list)
        res_str = print_binary_tree(res)
        print(res_str)