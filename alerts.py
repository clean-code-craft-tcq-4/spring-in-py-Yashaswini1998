def EmailAlert():
        return 11

def LEDAlert():
    return 15

def StatsAlerter(maxT, eA):
    sa_list = []
    sa_list.checkAndAlert = [maxT, eA]
    return None

def checkAndAlert(threshold, email, led):
    if email >= threshold:
        self.emailAlert.emailSent = True
    else:
        emailAlert.emailSent = False