@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r main.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r app\decorators\__init__.py
env\Scripts\autopep8.exe -i -r app\decorators\decorator.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\filters.py
env\Scripts\autopep8.exe -i -r app\models\info.py
env\Scripts\autopep8.exe -i -r app\models\validators.py
env\Scripts\autopep8.exe -i -r app\tests\__init__.py
env\Scripts\autopep8.exe -i -r app\tests\test_validators.py
env\Scripts\autopep8.exe -i -r app\tests\test_info.py
env\Scripts\autopep8.exe -i -r app\tests\test_filters.py
env\Scripts\autopep8.exe -i -r app\tests\test_decorator.py
pause
ECHO -----------------------------------------
ECHO Runing flake8...
ECHO -----------------------------------------
env\Scripts\flake8.exe main.py
env\Scripts\flake8.exe app\__init__.py
env\Scripts\flake8.exe app\decorators\__init__.py
env\Scripts\flake8.exe app\decorators\decorator.py
env\Scripts\flake8.exe app\models\__init__.py
env\Scripts\flake8.exe app\models\filters.py
env\Scripts\flake8.exe app\models\info.py
env\Scripts\flake8.exe app\models\validators.py
env\Scripts\flake8.exe app\tests\__init__.py
env\Scripts\flake8.exe app\tests\test_validators.py
env\Scripts\flake8.exe app\tests\test_info.py
env\Scripts\flake8.exe app\tests\test_filters.py
env\Scripts\flake8.exe app\tests\test_decorator.py
pause
pause
ECHO -----------------------------------------
ECHO Runing PyLint...
ECHO -----------------------------------------
env\Scripts\pylint.exe main.py
env\Scripts\pylint.exe app\__init__.py
env\Scripts\pylint.exe app\decorators\__init__.py
env\Scripts\pylint.exe app\decorators\decorator.py
env\Scripts\pylint.exe app\models\__init__.py
env\Scripts\pylint.exe app\models\filters.py
env\Scripts\pylint.exe app\models\info.py
env\Scripts\pylint.exe app\models\validators.py
env\Scripts\pylint.exe app\tests\__init__.py
env\Scripts\pylint.exe app\tests\test_validators.py
env\Scripts\pylint.exe app\tests\test_info.py
env\Scripts\pylint.exe app\tests\test_filters.py
env\Scripts\pylint.exe app\tests\test_decorator.py
pause
pause