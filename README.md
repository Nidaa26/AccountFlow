# Accounts Microservice REST API

![CI Build](https://github.com/nidaa26/AccountFlow/actions/workflows/ci-build.yaml/badge.svg)

> Replace `nidaa26/AccountFlow` above with your actual GitHub
> username/repo name so the badge points at your own Actions run. The badge
> turns green automatically the first time `ci-build.yaml` finishes
> successfully on `main`.

## Overview

A Flask-based REST API microservice that lets client applications **Create,
Read, Update, Delete, and List** customer Accounts. Built as part of an
Agile/DevOps capstone project: TDD-driven development, CI with GitHub Actions,
security headers via Flask-Talisman, containerization with Docker, and
deployment to Kubernetes/OpenShift via a Tekton CD pipeline.

## Endpoints

| Method | Endpoint              | Description                  |
|--------|------------------------|-------------------------------|
| GET    | `/`                    | Service info                 |
| GET    | `/health`               | Health check                 |
| POST   | `/accounts`             | Create a new account         |
| GET    | `/accounts`             | List all accounts            |
| GET    | `/accounts/<id>`        | Read a single account        |
| PUT    | `/accounts/<id>`        | Update an existing account   |
| DELETE | `/accounts/<id>`        | Delete an account            |

## Local Setup

```bash
pip install -r requirements.txt
nosetests
honcho start
```

## Tech Stack

Python, Flask, Flask-SQLAlchemy, Flask-Talisman, Flask-CORS, PostgreSQL,
Docker, Kubernetes/OpenShift, Tekton, GitHub Actions.
