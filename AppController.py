from AppView import AppView
from AppModel import AppModel

class AppController:

    def __init__(self, view: AppView, model: AppModel):
        self._view = view
        self._model = model

    def init(self):
        self._view.show_title()
        borough_option, vehicle_option, month_option, day_option = self._view.show_options()
        prediction = self._model.read_prediction(
            borough_option, vehicle_option, month_option, day_option
        )
        self._view.show_prediction(prediction)