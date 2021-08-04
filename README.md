# computer_database_testing
Testing related to test website for computers database

---

## Dependencies:

| No | Package |
| --- | ---- |
| 1 | `beautifulsoup4==4.9.3` |
| 2 |`certifi==2021.5.30` |
| 3 | `charset-normalizer==2.0.4` |
| 4 |`idna==3.2` |
| 5 |`requests==2.26.0` |
| 6 | `selenium==3.141.0`|
|7 | `soupsieve==2.2.1`|

----

## How to run?

> You need to have `docker` and `docker-compose` packages on your device before installation. If you don't have option to do so, plase contact me and I'll show you it.

| Step | Command | Details |
|---|---| --- |
|1. | `python3 -m venv venv` or `python -m venv venv` | Creation virtual environment in order not to waste |
|2.| `source venv/bin/activate`| Activating Virtual Environment|
|3. | `pip3 install -r requirements` | reading lines from requirements and installing them. (it can be `pip`)
| 4. | `docker-compose up` | for building standalone local server |
| 5. |`python3 path_to_source folder/source/test_suite.py` | Running python test suit |