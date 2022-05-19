import numpy as np

def calculateStats(numbers):
    if len(numbers) == 0:
        return float('NaN')
    else:
        l_avg = np.average(numbers)
        l_max = max(numbers)
        l_min = min(numbers)
        dict_Stats = {'avg': l_avg, 'max': l_max, 'min': l_min}    
    
    return dict_Stats
class EmailAlert:
    def __init__(self):
        self.emailSent = False
class LEDAlert:
    def __init__(self):
        self.ledGlows = False
class StatsAlerter:
    def __init__(self, maxThreshold, Alerts):
        self.maxThreshold = maxThreshold
        self.emailAlert: EmailAlert = Alerts[0]
        self.LEDAlert: LEDAlert = Alerts[1]

    def checkAndAlert(self, new_list):
        Stat_Dict = calculateStats(new_list)

        if Stat_Dict['max'] >= self.maxThreshold:
            self.emailAlert.emailSent = True
            self.LEDAlert.ledGlows = True
            