# Log Analyzer Report

## Setting Up Project

VirtualBox and Vagrant should already be installed. If they're not already in stalled please follow the
instructions on the Udacity website

    https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0

You will need to download the data

    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Open a terminal and process the following commands

    vagrant up
    vagrant ssh

Once in the vagrant shell do the following:

    cd /vagrant
    psql -d news -f newsdata.sql
    psql -d news -f newsviews.sql

## Running the Analyzer Report

Enter the following command to run the analyzer report

    ./log.py

