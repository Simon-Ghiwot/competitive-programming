class Solution:
    def simplifyPath(self, path: str) -> str:
        path_ = path.split("/")
        stack = []
        for i in range(len(path_)):
            if path_[i] == "/" or path_[i] == "" or path_[i] == ".":     
                continue

            if path_[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path_[i])
        return "/" + "/".join(stack)
            
