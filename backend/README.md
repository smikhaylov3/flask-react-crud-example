# Flask Backend Deployment

THe backend uses [Model](./dbms) to implement [API](../docs), have a look at [main.py](./main.py)

## Run existing Backend Server

### Setup Server

```shell
python3 -m venv python_modules          # create python environment
source ./python_modules/bin/activate    # activate python environment
python3 -m pip install -r package-lock.txt   # install python modules from package.txt
deactivate                              # deactivate python environment
```

```shell
ppm install
```

### Run Server

```shell 
source ./python_modules/bin/activate    # activate python environment
python main.py                          # run back-end server
deactivate                              # deactivate python environment
```

```shell
ppm start
```

### Install new-package

```shell
source ./python_modules/bin/activate    # activate python environment
pip install new-package				# install new-package
python -m pip freeze > package-lock.txt		# save new-package to package.txt
deactivate                              # deactivate python environment
```

```shell
ppm install new-package
```

## Create Backend from scratch

### Prerequisite

- [Anaconda (Python 3)](https://www.anaconda.com/distribution/#download-section)

### Create Flask App

```shell
mkdir backend
cd backend
python3 -m venv python_modules          # create python environment
source ./python_modules/bin/activate    # activate python environment
pip install flask flask-cors     		# install essitial modules
python -m pip freeze > package-lock.txt		# save dependencies to package.txt
deactivate                              # deactivate python environment
```

```shell
mkdir backend
cd backend
ppm install
ppm install flask flask-cors           # install essitial modules
```


## References

- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
