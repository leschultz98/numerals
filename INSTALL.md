# Guide for Installation
The code was tested on Ubuntu 16.04, with Python 3.7.3 and Pygame v1.9.6.

###1. Make sure you’ve got Python & pip
- Before you go any further, make sure you have Python and that it’s available from your command line. You can check this by simply running:
    ~~~
    $ python --version
    ~~~
- You should get some output like 3.7.3. If you do not have Python, please install the latest 3.x version from [python.org](https://python.org).
- Additionally, you’ll need to make sure you have pip available. You can check this by running:
    ~~~
    $ pip --version
    ~~~
- If you installed Python from source, with an installer from [python.org](https://python.org), you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately.

###2. Installing Pipenv
- Use pip to install Pipenv:
    ~~~
    $ pip install pipenv
    ~~~

###3. Clone repository
- Change the current working directory to the location where you want the cloned directory to be made.
    ~~~
    $ git clone http://gitlab-students.int.intek.edu.vn/mission/intek-mission-cardinal_numerals-playground/phuc_hoang.git
    ~~~

###4. Installing packages
- Install from Pipfile, if there is one:
    ~~~~
    $ pipenv install
    ~~~~ 
###5. Let's start
- Execute file `execute.py`.
    ~~~
    $ pipenv run python execute.py
Done !!!