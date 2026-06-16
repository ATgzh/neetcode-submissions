class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for x in range(len(position)):
            time = (target - position[x]) / speed[x]
            cars.append([position[x], time])

        cars.sort(reverse = True)
        fleet = 0
        slower = 0

        for pos, time in cars:
            if time > slower:
                fleet += 1
                slower = time
        return fleet