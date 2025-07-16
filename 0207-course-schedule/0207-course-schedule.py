class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        graph = defaultdict(list)

        # build graph
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses  

        def dfs(node):
            if state[node] == 1:
                return False  # circle
            if state[node] == 2:
                return True   # finish

            state[node] = 1  # now
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2  # visit
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True
