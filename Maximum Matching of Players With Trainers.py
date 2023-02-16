class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainer = result = 0
        players.sort()
        trainers.sort()
        
        for i in range(len(players)):
            while trainer < len(trainers) and trainers[trainer] <  players[i]:
                trainer += 1
            if trainer < len(trainers):
                result += 1
            trainer += 1

        return result
