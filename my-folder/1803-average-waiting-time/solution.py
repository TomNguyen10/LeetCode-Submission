class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        current = customers[0][0]
        for customer in customers:
            if current >= customer[0]:
                total += current - customer[0]
                current += customer[1]
            else:
                current = customer[0] + customer[1]
            total += customer[1]
            print(current)
        return total / len(customers)
        
