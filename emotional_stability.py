# Trying to simulate emotional stability and mental health in Python to enhance understanding of how it gets affected by various events.

emotional_stabilility = 0
useless_information = 0
negative_outlook = 0
positive_outlook = 0

def shifting_center_of_priorities(intensity):
    useless_information += intensity

def self_work(intensity):
    positive_outlook += intensity

def center_of_priorities():
    emotional_stabilility = 0 - negative_outlook + positive_outlook
    print(emotional_stabilility)
