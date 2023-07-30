@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe app.py
env\Scripts\flake8.exe app\__init__.py
env\Scripts\flake8.exe app\__main__.py
env\Scripts\flake8.exe app\app.py
env\Scripts\flake8.exe app\controllers\__init__.py
env\Scripts\flake8.exe app\controllers\base_controller.py
env\Scripts\flake8.exe app\controllers\recital.py
env\Scripts\flake8.exe app\decorators\__init__.py
env\Scripts\flake8.exe app\decorators\decorators_random.py
env\Scripts\flake8.exe app\helpers\__init__.py
env\Scripts\flake8.exe app\interfaces\__init__.py
env\Scripts\flake8.exe app\interfaces\base_controller.py
env\Scripts\flake8.exe app\interfaces\base_model.py
env\Scripts\flake8.exe app\interfaces\base_view.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\base_model.py
env\Scripts\flake8.exe app\models\queues.py
env\Scripts\flake8.exe app\models\recital.py
env\Scripts\flake8.exe app\models\random_data.py
env\Scripts\flake8.exe app\models\entities\__init__.py
env\Scripts\flake8.exe app\views\__init__.py
env\Scripts\flake8.exe app\views\base_view.py
env\Scripts\flake8.exe app\views\recital.py
env\Scripts\flake8.exe app\views\stage.py
env\Scripts\flake8.exe app\views\stage_logo.py
env\Scripts\flake8.exe tests\__init__.py
env\Scripts\flake8.exe tests\test_default.py
pause