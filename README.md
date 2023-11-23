# Doctor AI
For Lighspeed Gen AI Hackathon. A guardian for the patient.

Pull this docker image from docker hub:     
```
yalex778/can_rise_paco_ubuntu_dev:latest
```
For Mac user:
Install Pulseaudio on host computer

Launch the container:
```
docker run -it -d --privileged
           -v <your path>/doctor-ai:/doctor-ai
           -v ~/.config/pulse:/root/.config/pulse
           -p 9000:5000
           -p 9001:5001
           -e PULSE_SERVER=host.docker.internal
           --name doctor-ai
           yalex778/can_rise_paco_ubuntu_dev bash
```

Set Shell environment:                                  
```
export OPENAI_API_KEY=<Your API KEY>
```

In the root directory of doctor-ai, start the backend                                                
```
python main.py
```
                      
In the frontend directory, start the frontend                                                       
```
npm run dev
```

Open browser at:
```
http://localhost:9001
```

Test audio:                                             
                                 
Click the start button, switch to the doctor companion tab, start speaking, the transcribed text should be printed on the bottom console.
