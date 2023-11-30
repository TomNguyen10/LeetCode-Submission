class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        train = 0
        for i in range(len(energy)):
            if initialExperience <= experience[i]:
                diff = experience[i] - initialExperience
                train += diff + 1
                initialExperience += diff + 1
            if initialEnergy <= energy[i]:
                diff = energy[i] - initialEnergy
                train += diff + 1
                initialEnergy += diff + 1
            initialEnergy -= energy[i]
            initialExperience += experience[i]
        return train

        
