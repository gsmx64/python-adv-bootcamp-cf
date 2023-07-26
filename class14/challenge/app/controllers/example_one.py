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
        super().execute()

        self.pmvcs_view.clean_screen()
        print(self.pmvcs_view.get_intro())

        filters = self.pmvcs_helper.load_helper('filters', True)
        value = str('5')
        print("filters = self.pmvcs_helper.load_helper('filters', True)")
        print(f"filters.data_type(str('5')): {filters.data_type(value)}")
        print(f"filters type(): {type(filters.data_type(value))}")

        self.pmvcs_view.input_pause()
        # >>> to here!

        return False
