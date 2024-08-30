class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        employee_times = defaultdict(list)
    
        for name, time in access_times:
            employee_times[name].append(int(time))
    
        high_access_employees = []
    
        for name, times in employee_times.items():
            times.sort()
        
            for i in range(len(times) - 2):  
                if times[i + 2] - times[i] < 100:  
                    high_access_employees.append(name)
                    break  
    
        return high_access_employees
