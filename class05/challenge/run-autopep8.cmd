@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r env\Scripts\pylint.exe app\__main__.py
env\Scripts\autopep8.exe -i -r env\Scripts\pylint.exe app\app.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\base_controller.py
env\Scripts\autopep8.exe -i -r app\controllers\binary_search.py
env\Scripts\autopep8.exe -i -r app\decorators\__init__.py
env\Scripts\autopep8.exe -i -r app\decorators\decorators_random.py
env\Scripts\autopep8.exe -i -r app\helpers\__init__.py
env\Scripts\autopep8.exe -i -r app\interfaces\__init__.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_controller.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_model.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_view.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\base_model.py
env\Scripts\autopep8.exe -i -r app\models\binary_search.py
env\Scripts\autopep8.exe -i -r app\models\random_data.py
env\Scripts\autopep8.exe -i -r app\models\validations.py
env\Scripts\autopep8.exe -i -r app\models\entities\__init__.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\base_view.py
env\Scripts\autopep8.exe -i -r app\views\binary_search.py
env\Scripts\autopep8.exe -i -r tests\__init__.py
env\Scripts\autopep8.exe -i -r tests\test_default.py
pause