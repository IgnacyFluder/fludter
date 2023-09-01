import deepfakeecg

#deepfakeecg.generate("number of ECG to generate", "Path to generate", "start file ids from this number", "device to run") 

deepfakeecg.generate(5, "./deepfakes", start_id=0, run_device="cpu") # Generate 5 ECGs to the current folder starting from id=0
g = deepfakeecg.Generator()
