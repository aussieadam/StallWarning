class FlightData:

    def __init__(self, flight_id, initial_alt, alt_noise, alt_noise_buffet, time_to_buffet,
                 time_from_buffet_to_uncommanded_descent, magnitude_of_uncommanded_descent,
                 time_from_buffet_to_uncommanded_roll, magnitude_of_uncommanded_roll, initial_airspeed, airspeed_noise,
                 period_of_uncommanded_roll, time_from_buffet_to_uncommanded_descent_high,
                 magnitude_of_uncommanded_descent_high, time_from_buffet_to_positive_angle_of_attack,
                 max_angle_of_attack, rate_of_change_in_angle_of_attack):
        self.rate_of_change_in_angle_of_attack = rate_of_change_in_angle_of_attack
        self.max_angle_of_attack = max_angle_of_attack
        self.time_from_buffet_to_positive_angle_of_attack = time_from_buffet_to_positive_angle_of_attack
        self.magnitude_of_uncommanded_descent_high = magnitude_of_uncommanded_descent_high
        self.time_from_buffet_to_uncommanded_descent_high = time_from_buffet_to_uncommanded_descent_high
        self.period_of_uncommanded_roll = period_of_uncommanded_roll
        self.airspeed_noise = airspeed_noise
        self.initial_airspeed = initial_airspeed
        self.magnitude_of_uncommanded_roll = magnitude_of_uncommanded_roll
        self.time_from_buffet_to_uncommanded_roll = time_from_buffet_to_uncommanded_roll
        self.magnitude_of_uncommanded_descent = magnitude_of_uncommanded_descent
        self.time_from_buffet_to_uncommanded_descent = time_from_buffet_to_uncommanded_descent
        self.time_to_buffet = time_to_buffet
        self.alt_noise_buffet = alt_noise_buffet
        self.alt_noise = alt_noise
        self.initial_alt = initial_alt
        self.flight_id = flight_id


