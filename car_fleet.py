class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # They can't pass, so i need to prioritize the furthest car
        # max in position array

        # O(nlogn)
        # sort position array descending with attached original indeces
        # (max, o_inx),(no.2, o_idx2), etc

        # O(n)
        # now find if proceeding cars 'catch' current car
        # current car T.T.T. (turns till target) <= next car TTT
        # TTT = ceiling(target - position / speed)
        # if so, same fleet, if not, new fleet

        # return fleet count

        # Overall: O(nlogn) from sort

        # O(n)
        pos_ttt = []
        for idx, pos in enumerate(position):
            ttt = (target - pos) / speed[idx]
            pos_ttt.append((pos, ttt))
        
        # O(nlogn)
        sorted_pos = sorted(pos_ttt, key=lambda tup: tup[0])

        fleets = 1
        curr_fleet = sorted_pos.pop()
        # O(n)
        while sorted_pos:
            next_car = sorted_pos.pop()
            if curr_fleet[1] < next_car[1]:
                curr_fleet = next_car
                fleets += 1
        
        return fleets