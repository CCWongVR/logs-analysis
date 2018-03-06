# Udacity Logs Analysis

A simple python tool to interpret data from an internal database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need:

```
Python 2
Virtual Box
Vagrant
[Udacity News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
```
## Running the script

Do the following to run the analysis tool

### Getting into Postgresql

Open cmd line where vagrant is installed and run the VM

```
vagrant up
```

Log in to the VM

```
vagrant ssh
```

Move into the shared vagrant folder

```
cd /vagrant
```

Enter Postgresql and the news DB

```
psql -d news -f newsdata.sql
```

### Views

You will need two views to run the python script:

```
create view total_status as
select time::date as day, count(status) as t_count from log group by day;
```

and

```
create view error_status as
select time::date as day, count(status) as e_count from log where status like '%404%' group by day;
```

These can simply be pasted into the cmd line when in psql and executed.

### Running the script

To run our python script, first exit psql

```
ctrl + D
```

Run the script

```
python logsanalysis.py
```

## Acknowledgments

* Udacity
* Perry McManis for sql syntax help
* Official Python documentation
