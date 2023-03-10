class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = []
        for i in range(len(position)):
            combine.append([position[i], speed[i]])
        combine.sort(reverse = True)

        # implement solution using speed = change in position / time
        fleets = []
        for i in range(len(position)):
            time = (target - combine[i][0]) / combine[i][1]

            if not fleets or fleets and time > fleets[-1]:
                fleets.append(time)

        return len(fleets)
