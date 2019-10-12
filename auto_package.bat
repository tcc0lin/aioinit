
pip uninstall .\dist\aiohttp_init-0.0.1-py3-none-any.whl
python setup.py bdist_wheel
pip install .\dist\aiohttp_init-0.0.1-py3-none-any.whl


REM twine upload dist/*