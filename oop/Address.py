class Address:
    def __init__(self, cityName, countryName, houseNumber, street, state):
        self.cityName = cityName
        self.countryName = countryName
        self.houseNumber = houseNumber
        self.street = street
        self.state = state

    def set_city_name(self, cityName):
        self.cityName = cityName

    def set_country_name(self, countryName):
        self.countryName = countryName

    def set_house_number(self, houseNumber):
        self.houseNumber = houseNumber

    def set_street(self, street):
        self.street = street

    def set_state(self, state):
        self.state = state

    def get_city_name(self):
        return self.cityName

    def get_country_name(self):
        return self.countryName

    def get_house_number(self):
        return self.houseNumber

    def get_street(self):
        return self.street

    def get_state(self):
        return self.state
