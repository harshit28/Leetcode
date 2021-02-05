class Solution:
    def simplifyPath(self, path: str) -> str:
        patharray = path.split('/')
        stack = []
        for elem in patharray:
            if stack and elem == "..":
                stack.pop()
            elif elem != "." and elem !=".." and elem!="":
                stack.append(elem)
                
        return "/" + "/".join(stack)
