# An attempt to understand and explore Airflow
## Setting up the airflow environment:  

`./bootstrap`  

`source pyenv/bin/activate`

Before you initialize db with next command, make sure that the directory "~/airflow" exists and file "~/airflow/airflow.cfg" has following options properly set:

    dags_folder = dag directory path of this project  
    load_examples = False (This is optional to avoid confusion with airflow implemented dags)  
    executor = LocalExecutor  
We are using LocalExecutor as we are exploring airflow and haven't really moved to production deployment yet.

To init the airflow db  
`fab initdb`

Following  will run airflow webserver and you can check ui on localhost:8083  
`fab runserver`  
**Note that above command wont run in background so you need another terminal window and run following command in it.**  
`source pyenv/bin/activate`

## Project structure:

You can take a look at example implementation of dags in directory "airflow-for-workflows/dags"
Following command will run unit tests but we don't have any yet :(.  
`fab test`

Feel free to explore new operator and add example implementation here.

## Running existing implementations:

You can simply try out example dags from "dags" directory using following command and observe it in UI(localhost:8083)  
`airflow backfill airflow_retry_feature -s 2016-03-20T00 -e 2016-03-20T01`
