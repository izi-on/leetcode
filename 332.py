from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        mapToPossible = {}
        countLeft = len(tickets)
        for ticket in tickets:
            if ticket[0] not in mapToPossible:
                mapToPossible[ticket[0]] = defaultdict(int)
            mapToPossible[ticket[0]][ticket[1]] = (
                mapToPossible[ticket[0]][ticket[1]] + 1
            )

        def dfs(curTrajectory: list[str], countLeft: int):
            nonlocal mapToPossible
            # print(curTrajectory)
            if countLeft == 0:
                # print("Found!")
                return curTrajectory
            curAP = curTrajectory[-1]
            possibleFlights = (
                mapToPossible[curAP].keys() if curAP in mapToPossible else []
            )
            sPF = list(possibleFlights)
            heapq.heapify(sPF)
            while len(sPF) > 0:
                flight = heapq.heappop(sPF)
                if mapToPossible[curAP][flight] == 0:
                    continue
                mapToPossible[curAP][flight] = mapToPossible[curAP][flight] - 1
                curTrajectory.append(flight)
                res = dfs(curTrajectory, countLeft - 1)
                if res is not None:
                    return res
                curTrajectory.pop()
                mapToPossible[curAP][flight] = mapToPossible[curAP][flight] + 1
            return None

        return dfs([start], countLeft)
