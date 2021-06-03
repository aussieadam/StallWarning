import time
import random
from dcd.FlightData import FlightData
import numpy as np


def generate_flight_record(flight_id):
    initial_alt = random.randint(5000, 43000)
    alt_noise = np.random.normal(0, 5, 1)
    alt_noise_buffet = np.random.normal(0, 10, 1)
    time_to_buffet = random.randint(0, 100)
    time_from_buffet_to_uncommanded_descent = random.randint(0, 10)
    magnitude_of_uncommanded_descent = random.randint(time_from_buffet_to_uncommanded_descent,
                                                      time_from_buffet_to_uncommanded_descent + 300)
    time_from_buffet_to_uncommanded_roll = random.randint(time_from_buffet_to_uncommanded_descent,
                                                          time_from_buffet_to_uncommanded_descent + 30)
    magnitude_of_uncommanded_roll = random.randint(0, 90)
    initial_airspeed = random.randint(120, 300)
    airspeed_noise = np.random.normal(0, 5, 1)
    period_of_uncommanded_roll = np.random.normal(0, 10, 1)
    time_from_buffet_to_uncommanded_descent_high = random.randint(time_from_buffet_to_uncommanded_descent,
                                                                  time_from_buffet_to_uncommanded_descent + 30)
    magnitude_of_uncommanded_descent_high = random.randint(120, 1200)
    time_from_buffet_to_positive_angle_of_attack = random.randint(time_from_buffet_to_uncommanded_descent,
                                                                  time_from_buffet_to_uncommanded_descent + 10)
    max_angle_of_attack = random.randint(0, 30)
    rate_of_change_in_angle_of_attack = random.random()

    return FlightData(flight_id, initial_alt, alt_noise, alt_noise_buffet, time_to_buffet,
                      time_from_buffet_to_uncommanded_descent, magnitude_of_uncommanded_descent,
                      time_from_buffet_to_uncommanded_roll, magnitude_of_uncommanded_roll, initial_airspeed,
                      airspeed_noise,
                      period_of_uncommanded_roll, time_from_buffet_to_uncommanded_descent_high,
                      magnitude_of_uncommanded_descent_high, time_from_buffet_to_positive_angle_of_attack,
                      max_angle_of_attack, rate_of_change_in_angle_of_attack)
