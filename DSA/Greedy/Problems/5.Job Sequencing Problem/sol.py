
class Solution:
    def JobScheduling(self, Jobs):
        # Sort jobs by decreasing profit
        Jobs.sort(key=lambda x: -x[2])

        n = len(Jobs)
        maxDeadline = max(job[1] for job in Jobs)

        # Initialize time slots as free
        slot = [-1] * maxDeadline
        count = 0
        profit = 0

        for job in Jobs:
            # Try to schedule job on or before its deadline
            for j in range(job[1] - 1, -1, -1):
                if slot[j] == -1:
                    slot[j] = job[0]  # job ID assigned
                    count += 1
                    profit += job[2]
                    break

        return [count, profit]

