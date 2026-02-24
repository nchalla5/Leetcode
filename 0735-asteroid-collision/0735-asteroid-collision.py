class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        neg = []
        i = 0
        while i < len(asteroids):
            # print(i)
            if asteroids[i] < 0:
                j = i - 1
                while j >= 0:
                    # print(j)
                    if asteroids[j] > 0:
                        if -asteroids[i] < asteroids[j]:
                            break
                        elif -asteroids[i] == asteroids[j]:
                            asteroids[j] = 0
                            break
                        else:
                            asteroids[j] = 0
                    j -= 1
                if j == -1:
                    neg.append(asteroids[i])
                asteroids[i] = 0
            i += 1
        pos = []
        for ast in asteroids:
            if ast != 0:
                pos.append(ast)
        return neg+pos




