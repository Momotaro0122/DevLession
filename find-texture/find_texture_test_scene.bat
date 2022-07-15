@ECHO OFF

SET current=%~dp0
SET test_py_script=%current%\texture_finder.py
SET test_scene=%current%\find_texture_test_scene.ma

IF EXIST %test_py_script% (
    IF EXIST %test_scene% (
        python %test_py_script% %test_scene%
    ) ELSE (
        ECHO %test_scene% is not found!
    )
) ELSE (
    ECHO %test_py_script% is not found!
)
