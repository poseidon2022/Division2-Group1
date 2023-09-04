class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        mine = defaultdict(list)
        for i,j in prerequisites:
            mine[i].append(j)
        if not prerequisites:
            return True
        def helper(i,visited,recursion_stack):
            if i in recursion_stack:
                return False
            if i in visited:
                return True


            visited.add(i)
            recursion_stack.add(i)
            for j in mine[i]:
               if not helper(j, visited, recursion_stack):
                    return False

            recursion_stack.remove(i)
            return True
        
        for i in range(numCourses):
            if not helper(i, visited, set()):
                return False
        
        return True