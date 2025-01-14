class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # dict of letters -> wait time, amt remaining
        # O(max same tasks count * n)
        # for each cycle (while dict not empty)
            # O(unique tasks)
            # use all letters with 0 wait time remaining
            # reset cd timer to n
            # decrease timer on all other letters
        # return num cycles when dict empty

        # hash of processing task -> wait time
        # hash of waiting task -> amt remaining
        # O(tasks)
        # for each task t
            # if task is in process, put into waiting (increment amt if in waiting)
            # else add to processing, increment cycle count
        # O(max same tasks * n)
        # while processing
            # for each task in processing
                # decrement wait time of task
                # if time == 0
                    # check if task waiting
                        # decrement amt in waiting
                        # increment cycles
                        # continue
                    # else delete process
            # increment cycles

        # return cycles

        ### FINAL SOLUTION

        # the last cycle is determined by the max letter count
        # cycles = (max(letter_count) - 1) * (n + 1) + num_max_letters

        # hash task -> count
        # O(num_tasks)
        # for each task t
            # add to hash or increment count

        # O(unique tasks)
        # max_count = 0
        # num_max_letters = 1
        # for each task in hash
            # if count > max_count:
                # max_count = count
                # num_max_letters = 1
            # if count == max_count:
                #num_max_letters += 1
        
        # return max_count - 1 * (n + 1) + num_max_letters
        task_counts = {}
        for t in tasks:
            if t in task_counts:
                task_counts[t] += 1
            else:
                task_counts[t] = 1
        
        max_count = 0
        num_letters = 1
        for count in task_counts.values():
            if count > max_count:
                max_count = count
                num_letters = 1
            elif count == max_count:
                num_letters += 1
        
        return max(len(tasks), (max_count - 1) * (n+1) + num_letters)