class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        neg = []
        pos = deque()
        i = 0
        while i < len(asteroids):
            # print(i)
            if asteroids[i] < 0:
                j = len(pos) - 1
                while j >= 0:
                    if -asteroids[i] < pos[j]:
                        break
                    elif -asteroids[i] == pos[j]:
                        pos.pop()
                        break
                    else:
                        pos.pop()
                    j -= 1
                if j == -1:
                    neg.append(asteroids[i])
            else:
                pos.append(asteroids[i])
            i += 1
        return neg+list(pos)




