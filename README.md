# paco
For Lighspeed Gen AI Hackathon. A guardian for the patient.

Pull this docker image:     
```
yalex778/can_rise_paco_ubuntu_dev:latest
```
For Mac user:
Install Pulseaudio on host computer

Launch the container:
```
docker run -it -d --privileged
           -v <your path>/paco-main:/paco-main
           -v ~/.config/pulse:/root/.config/pulse
           -p 9000:5000
           -p 9001:5001
           -e PULSE_SERVER=host.docker.internal
           --name doctor-ai
           yalex778/can_rise_paco_ubuntu_dev bash
```

In the root directory of doctor-ai:    
Start the backend    
```
python main.py
```

In the frontend directory:    
```
npm run dev
```

Open browser at:
```
http://localhost:9001
```
