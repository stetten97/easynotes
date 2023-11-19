# Documentation
This repository contains a dockerized `Flask` application that enables the user to take notes which can be stored in project-specific notebooks.

## Implementation
The application uses `Flask` blueprints to enable an easy way of modular development of additional features.
All notebooks and notes are stored in a `sqlite` database within the `Docker` container. The DB schema is based on models implemented in `Flask`. All editing features (e.g. adding notebooks/notes, modifying content and names) are implemented within specific view functions as well as with some basic `JavaScript` to enable in-place editing with `AJAX` requests.

## Running the app locally
To run the application locally, create a clone and run:
```
sudo docker compose build && docker compose up
```
Make sure, that you have `Docker Desktop` installed on your local machine. The server will run on localhost port 5000 by default, which can be easily changed in the `docker-compose.yml` as well as in the entry point of the application. The app is currently not deployed anywhere.\

To enter a bash terminal within the container, run:
```
docker exec -it easynotes-easynotes-1 bash
```