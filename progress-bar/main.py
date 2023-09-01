from tqdm import tqdm
import time

for i in tqdm(range(101), desc="Loading…", ascii=False, ncols=75):
    time.sleep(0.01)

print("Complete.")

for i in tqdm(range(101), desc="Loading…", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"):
    time.sleep(0.01)

print("Complete custom.")