class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination>start:
            left= sum(distance[start:destination])
            right= sum(distance[:start] + distance[destination:])
            return min(left,right)
        else:
            start, destination = destination, start
            left= sum(distance[start:destination])
            right= sum(distance[:start] + distance[destination:])
            return min(left,right)