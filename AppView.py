import streamlit as st

class AppView:

    def __init__(self):
        self._city_borough = ['Wandsworth', 'Bexley', 'Lambeth', 'City of Westminster', 'Barking and Dagenham', 'Camden',
                        'Greenwich',
                        'Newham', 'Tower Hamlets', 'Barnet', 'Hounslow', 'Kingston', 'Kensington and Chelsea',
                        'Islington',
                        'Brent', 'Haringey', 'Bromley', 'Merton', 'Hackney', 'Southwark', 'Ealing', 'Sutton',
                        'Hammersmith and Fulham', 'Havering', 'Hillingdon', 'Waltham Forest', 'Richmond upon Thames',
                        'Redbridge', 'City of London', 'Lewisham', 'Croydon', 'Harrow', 'Enfield']
        self._vehicle_type = ['HeavyGoodsVehicle', 'PrivateHireCarLicensed', 'OtherMotorVehicle', 'RiddenHorse', 'Car',
                        'Taxi',
                        'OtherNonMotorVehicle', 'Motorcycle_500cc_Plus', 'BusOrCoach', 'PedalCycle',
                        'Motorcycle_0_50cc',
                        'LightGoodsVehicle', 'Motorcycle_50_125cc', 'Motorcycle_125_500cc', 'Minibus',
                        'AgriculturalVehicle',
                        'MediumGoodsVehicle', 'TramOrLightRail']
        self._months_list = list(range(1, 13))
        self._days_list = list(range(1, 32))

    def show_title(self):
        st.title("Prediction of Accident in London")

    def show_options(self):
        borough_option = st.selectbox('Region', tuple(self._city_borough))
        vehicle_option = st.selectbox('Vehicle', tuple(self._vehicle_type))
        month_option = st.selectbox('Month', tuple(self._months_list))
        day_option = st.selectbox('Day', tuple(self._days_list))

        return (borough_option, vehicle_option,
                month_option, day_option)

    def show_prediction(self, result):
        if result == 0:
            prediction = "Slight"
        elif result == 1:
            prediction = "Fatal"
        elif result == 2:
            prediction = "Serious"
        else:
            prediction = "Unknown"

        st.write(f"Possible Severity: {prediction}")
