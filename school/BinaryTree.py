class BinaryTree:
    class Node:         # 노드 생성자
        def __init__(self, item, left = None, right = None):
            self.item = item            # 항목
            self.left = left            # 왼쪽 노드
            self.right = right          # 오른쪽 노드

    def __init__(self):
        self.root = None                # 트리 루트

    def preorder(self, n):                  # 전위순회
        if n != None:
            print(str(n.item), ' ', end='')     # 노드 먼저 방문
            if n.left:
                self.preorder(n.left)           # 왼쪽 서브트리 방문
            if n.right:
                self.preorder(n.right)          # 후에 오른쪽 서브트리 방문

    def inorder(self, n):               # 중위순회
        if n != None:
            if n.left:                          # 왼쪽 서브트리 먼저 방문
                self.inorder(n.left)
            print(str(n.item), ' ', end='')     # 노드 방문
            if n.right:
                self.inorder(n.right)           # 후에 오른쪽 서브트리 방문

    def postorder(self, n):             # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)          # 왼쪽 서브트리 먼저 방문
            if n.right:
                self.postorder(n.right)         # 오른쪽 서브트리 방문
            print(str(n.item), ' ', end='')     # 마지막으로 노드 방문

    def levelorder(self, root):         # 레벨순회
        q = []
        q.append(root)                          # 자료구조의 큐 구조를 이용하려 트리 구현
        while len(q) != 0:
            t = q.pop(0)                        # 큐의 첫 항목 삭제
            print(str(t.item), ' ', end='')     # 삭제된 노드 방문
            if t.left != None:
                q.append(t.left)                # 왼쪽 자식 노드 큐에 삽입
            if t.right != None:
                q.append(t.right)               # 오른쪽 자식 노드 큐에 삽입

    def height(self, root):             # 트리 높이 계산
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1     # 두 자식노드의 높이 중 큰 높이 + 1
