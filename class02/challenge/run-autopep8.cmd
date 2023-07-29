@ECHO OFF
::env\Scripts\activate
ECHO -----------------------------------------
ECHO Runing AutoPEP8...
ECHO -----------------------------------------
env\Scripts\autopep8.exe -i -r app.py
env\Scripts\autopep8.exe -i -r app\__init__.py
env\Scripts\autopep8.exe -i -r app\__main__.py
env\Scripts\autopep8.exe -i -r app\app.py
env\Scripts\autopep8.exe -i -r app\controllers\__init__.py
env\Scripts\autopep8.exe -i -r app\controllers\average_age_by_career.py
env\Scripts\autopep8.exe -i -r app\controllers\base_controller.py
env\Scripts\autopep8.exe -i -r app\controllers\careers_by_average_age.py
env\Scripts\autopep8.exe -i -r app\controllers\city_with_more_careers.py
env\Scripts\autopep8.exe -i -r app\controllers\students_by_age.py
env\Scripts\autopep8.exe -i -r app\controllers\students_by_average_age.py
env\Scripts\autopep8.exe -i -r app\controllers\students_by_city.py
env\Scripts\autopep8.exe -i -r app\controllers\students_by_country.py
env\Scripts\autopep8.exe -i -r app\controllers\students_cities_residence.py
env\Scripts\autopep8.exe -i -r app\decorators\__init__.py
env\Scripts\autopep8.exe -i -r app\helpers\__init__.py
env\Scripts\autopep8.exe -i -r app\helpers\csv.py
env\Scripts\autopep8.exe -i -r app\helpers\dict.py
env\Scripts\autopep8.exe -i -r app\helpers\export.py
env\Scripts\autopep8.exe -i -r app\helpers\json.py
env\Scripts\autopep8.exe -i -r app\helpers\screen.py
env\Scripts\autopep8.exe -i -r app\helpers\table.py
env\Scripts\autopep8.exe -i -r app\interfaces\__init__.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_controller.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_model.py
env\Scripts\autopep8.exe -i -r app\interfaces\base_view.py
env\Scripts\autopep8.exe -i -r app\models\__init__.py
env\Scripts\autopep8.exe -i -r app\models\average_age_by_career.py
env\Scripts\autopep8.exe -i -r app\models\base_model.py
env\Scripts\autopep8.exe -i -r app\models\careers_by_average_age.py
env\Scripts\autopep8.exe -i -r app\models\city_with_more_careers.py
env\Scripts\autopep8.exe -i -r app\models\data.py
env\Scripts\autopep8.exe -i -r app\models\students_by_age.py
env\Scripts\autopep8.exe -i -r app\models\students_by_average_age.py
env\Scripts\autopep8.exe -i -r app\models\students_by_city.py
env\Scripts\autopep8.exe -i -r app\models\students_by_country.py
env\Scripts\autopep8.exe -i -r app\models\students_cities_residence.py
env\Scripts\autopep8.exe -i -r app\models\entities\__init__.py
env\Scripts\autopep8.exe -i -r app\views\__init__.py
env\Scripts\autopep8.exe -i -r app\views\average_age_by_career.py
env\Scripts\autopep8.exe -i -r app\views\base_view.py
env\Scripts\autopep8.exe -i -r app\views\careers_by_average_age.py
env\Scripts\autopep8.exe -i -r app\views\city_with_more_careers.py
env\Scripts\autopep8.exe -i -r app\views\students_by_age.py
env\Scripts\autopep8.exe -i -r app\views\students_by_average_age.py
env\Scripts\autopep8.exe -i -r app\views\students_by_city.py
env\Scripts\autopep8.exe -i -r app\views\students_by_country.py
env\Scripts\autopep8.exe -i -r app\views\students_cities_residence.py
env\Scripts\autopep8.exe -i -r tests\__init__.py
pause