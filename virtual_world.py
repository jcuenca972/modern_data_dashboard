from AppView import AppView
from AppModel import AppModel
from AppController import AppController

if __name__ == "__main__":
    view = AppView()
    model = AppModel()
    controller = AppController(view, model)
    controller.init()