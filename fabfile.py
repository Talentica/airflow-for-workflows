from fabric.api import local

def test():
    local("nosetests")

def runserver():
    local("airflow webserver -p 8083")

# initialize the airflow database
def initdb():
    local("airflow initdb")
