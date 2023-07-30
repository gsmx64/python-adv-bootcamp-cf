@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe app.py
env\Scripts\pylint.exe app\__init__.py
env\Scripts\pylint.exe app\__main__.py
env\Scripts\pylint.exe app\app.py
env\Scripts\pylint.exe app\controllers\__init__.py
env\Scripts\pylint.exe app\controllers\base_controller.py
env\Scripts\pylint.exe app\controllers\recital.py
env\Scripts\pylint.exe app\decorators\__init__.py
env\Scripts\pylint.exe app\decorators\decorators_random.py
env\Scripts\pylint.exe app\helpers\__init__.py
env\Scripts\pylint.exe app\interfaces\__init__.py
env\Scripts\pylint.exe app\interfaces\base_controller.py
env\Scripts\pylint.exe app\interfaces\base_model.py
env\Scripts\pylint.exe app\interfaces\base_view.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\base_model.py
env\Scripts\pylint.exe app\models\queues.py
env\Scripts\pylint.exe app\models\recital.py
env\Scripts\pylint.exe app\models\random_data.py
env\Scripts\pylint.exe app\models\entities\__init__.py
env\Scripts\pylint.exe app\views\__init__.py
env\Scripts\pylint.exe app\views\base_view.py
env\Scripts\pylint.exe app\views\recital.py
env\Scripts\pylint.exe app\views\stage.py
env\Scripts\pylint.exe app\views\stage_logo.py
env\Scripts\pylint.exe tests\__init__.py
env\Scripts\pylint.exe tests\test_default.py
pause