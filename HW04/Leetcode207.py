# Runtime: 44 ms, faster than 89.32% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 84.51% of Python3 online submissions
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * (numCourses)
        graph = [[] for i in range(numCourses)]
        for course, preq in prerequisites:
            indegree[course] += 1
            graph[preq].append(course)

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        path = []
        while queue:
            curr = queue.pop(0)
            path.append(curr)
            courses = graph[curr]
            for course in courses:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return len(path) == numCourses