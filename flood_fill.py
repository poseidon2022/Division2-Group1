class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ind = len(image[0])
        whole = len(image)
        queue = deque()
        queue.append((sr,sc))
        value = image[sr][sc]
        if image[sr][sc]==color: return image
        while queue:
            cur = queue.popleft()
            image[cur[0]][cur[1]] = color
            if cur[0]-1>=0 and image[cur[0]-1][cur[1]]==value:
                queue.append((cur[0]-1,cur[1]))
            if cur[0]+1<whole and image[cur[0]+1][cur[1]]==value:
                queue.append((cur[0]+1,cur[1]))
            if cur[1]-1>=0 and image[cur[0]][cur[1]-1]==value:
                queue.append((cur[0],cur[1]-1))
            if cur[1]+1<ind and image[cur[0]][cur[1]+1]==value:
                queue.append((cur[0],cur[1]+1))
        return image