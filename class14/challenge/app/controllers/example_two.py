""" Example Two Controller file for PMVCS APP """
from app.controllers.base_controller import BaseController
from app.models.example_two import ExampleTwoModel
from app.views.example_two import ExampleTwoView


class ExampleTwoController(BaseController):
    """ Class for Example Two Controller """

    def __init__(self, **kwargs) -> None:
        """
        Init ExampleTwo Controller requirements
        """
        super().__init__(**kwargs)

        self.model = ExampleTwoModel(**kwargs)
        self.view = ExampleTwoView(**kwargs)

    def execute(self) -> str:
        """
        Execute Base Controller
        """
        # >>> Inserts your code from here...
        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        print('>>> Insert your code here!')

        self.pmvcs_view.input_pause()
        self.pmvcs_view.clean_screen()
        # >>> to here!

        return False
