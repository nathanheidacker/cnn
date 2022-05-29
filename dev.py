from data import ONCE
import os

data = ONCE("./data")

ids = []
for seq_id, frames in data.train_info.items():
    for frame_id in frames:
        ids.append((seq_id, frame_id))

for i, point_id in enumerate(ids):
    cloud = data.load_point_cloud(point_id[0], point_id[1])
    print(cloud.shape)
    if i == 10:
        break