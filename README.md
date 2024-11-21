# DaaS
This Project is about providing dashboard as a service where the business clients can use to look on the dashboard and also can get notification alerts with the integration of IOT devices and cloud virtual machines as well.

## Table of Contents
- [Pre-requisites]
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Pre-requisites
1.AWS Account 
2.Terraform & Docker installed on local machine
3.Github Repository for hosting the python code

- InfluxDB installed on a managed service
- Grafana connected to influxDB for visualization
- Github Actions enabled for CI/CD

## Creating directories and files in your local machines
mkdir app
mkdir grafana
mkdir grafana\provisioning
mkdir grafana\provisioning\datasources
mkdir grafana\provisioning\dashboards
mkdir terraform
mkdir .github
mkdir .github\workflows

New-Item -ItemType File app\app.py
New-Item -ItemType File app\Dockerfile
New-Item -ItemType File app\requirements.txt
New-Item -ItemType File grafana\provisioning\datasources\influxdb.yaml
New-Item -ItemType File grafana\provisioning\dashboards\dashboard.json
New-Item -ItemType File terraform\main.tf
New-Item -ItemType File terraform\variables.tf
New-Item -ItemType File terraform\outputs.tf
New-Item -ItemType File terraform\terraform.tfvars
New-Item -ItemType File .github\workflows\ci-cd.yml
New-Item -ItemType File docker-compose.yml
New-Item -ItemType File README.md

Get-ChildItem -Recurse

git init
git remote add origin https://github.com/pragadesh1/DaaS_Project
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

## purpose
app.py: Contains your IoT simulation script.
Dockerfile: Instructions to containerize your Python application.
requirements.txt: Python dependencies for the application.
influxdb.yaml: Automatically configure InfluxDB as a Grafana data source.
dashboard.json: (Optional) Define a pre-configured dashboard for Grafana.
main.tf: Contains the Terraform configuration to deploy AWS resources.
variables.tf: Define reusable variables for your infrastructure.
outputs.tf: Output values like the instance public IP for later use.
terraform.tfvars: Store actual variable values (e.g., AWS credentials, region).
ci-cd.yml: GitHub Actions workflow for automated builds, tests, and deployments.
touch docker-compose.yml
