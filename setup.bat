@echo off

REM --- Installation of requirements ---
echo Installing requirements from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 goto :requirements_error
echo Requirements installed successfully.
echo.

REM --- Execution of other setup scripts ---
echo Executing setup scripts...

echo Running seed_data.py...
python seed_data.py
if errorlevel 1 goto :seed_data_error
echo seed_data.py executed successfully.
echo.

echo Running download_nltk_resources.py...
python download_nltk_resources.py
if errorlevel 1 goto :resources_setup_error
echo download_nltk_resources.py executed successfully.
echo.

echo Setup complete!
goto :eof

:requirements_error
echo Error installing requirements. Please check requirements.txt.
goto :eof

:seed_data_error
echo Error executing seed_data.py.
goto :eof

:resources_setup_error
echo Error executing download_nltk_resources.py.
goto :eof

:eof