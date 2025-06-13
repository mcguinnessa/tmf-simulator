# tmf-simulator
Simulates (some) TMF APIs with dummy data


Run
===
python3 tmf_simulator_app.py


Docker
======
docker build -t mcguinnessa/tmf-simulator:latest .
docker run -p 8123:5000 --name tmf-simulator -d mcguinnessa/tmf-simulator:latest
docker stop  tmf-simulator; docker remove tmf-simulator
docker push mcguinnessa/tmf-simulator:latest



