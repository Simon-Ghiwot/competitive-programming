class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = {}

        for path in paths:
            directory = path.split()
            for i in range(1, len(directory)):
                size = len(directory[i])
                index = directory[i].find("(")
                file_name = directory[i][0 : index]
                file_content = directory[i][index + 1 : size - 1]
                if not map.get(file_content):
                    map[file_content] = []
                map[file_content].append(directory[0] + "/" + file_name)
                    
        result = []
        for key in map.keys():
            if len(map.get(key)) > 1:
                result.append(map.get(key))
        return result
