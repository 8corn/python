class BHeap:
    def __init__(self, a):                  # 이진힙 생성자
        self.a = a                          # 리스트 a
        self.N = len(a) - 1                 # 항목 수 N

    def create_heap(self):                  # 초기 힙 만들기
        for i in range(self.N//2, 0, -1):
            self.dewnheap(i)

    def insert(self, key_value):            # 삽입 연산
        self.N += 1
        self.a.append(key_value)                # 새 항목을 힙 마지막에 추가
        self.upheap(self.N)                     # 힙 속성 회복시키기 위해
        
    def delete_min(self):                   # 최솟값 삭제
        if self.N == 0:
            print('힙이 비어있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]   # a[1]과 a[N] 교환
        del self.a[-1]
        self.N -= 1
        self.downheap(1)                        # 힙속성 회복시키기 위해
        return minimum
    
    def downheap(self, i):                  # 힙 내려가면서 회복
        while 2*i <= self.N:
            k = 2*i                             # 왼쪽, 오른쪽 자식 중에서 승자 결정
            if k < self.N and self.a[k][0] > self.a[k + 1][0]:  # 힙속성 만족하면 루프 나가기
                k += 1  
            if self.a[i][0] < self.a[k][0]:     # 자식 승자와 현재 노드 교환
                break
            self.a[i], self.a[k] = self.a[k], self.a[i] # 자식 승자와 현재 노드 교환
            i = k

    def upheap(self, j):                    # 힙 올라가며 힙속성 회복
        while j > 1 and self.a[j//2][0] > self.a[j][0]: 
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]   # 부모와 자식 교환
            j = j//2                                # 현재 노드가 한 층 올라감

    def print_heap(self):                   # 힙 출력
        for i in range(1, self.N + 1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')
        print('\n 힙 크기 = ', self.N)