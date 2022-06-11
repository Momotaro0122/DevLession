::
:: Please complete this batch file and launch Python script in same directory.
:: Simple display "Hello, World" for practice.
::
::
:: Author : Martin Lee
:: Last Update : 2022-06-10
::
:: Turn off echo.
@ECHO OFF
:: Variables.
SET CURRENT=%~dp0
SET SCRIPT=%CURRENT%\hello_world.py 
:: See python file if exist or not.
IF EXIST %SCRIPT% (
    python %SCRIPT% ECHO %1
) ELSE (
    ECHO %SCRIPT% is not found!!
)