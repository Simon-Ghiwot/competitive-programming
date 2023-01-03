class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map = {}
        result = []
        for domain in cpdomains:
            count, domain = domain.split()
            domain_list = domain.split('.')
            for i in range(len(domain_list)):
                current_list = domain_list[i:]
                key = ".".join(current_list)
                map[key] = map.get(key, 0) + int(count)

        for key in map.keys():
            output = str(map.get(key)) + " " + key
            result.append(output)
        return result
