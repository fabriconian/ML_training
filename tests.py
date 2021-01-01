import gym
import os
import sys
import pdb

os.environ['LD_LIBRARY_PATH']='/home/bubuntu/.mujoco/mujoco200/bin/'
os.environ['DYLD_LIBRARY_PATH']='/home/bubuntu/.mujoco/mujoco200/bin/'
os.environ['MUJOCO_PY_MUJOCO_PATH']='/home/bubuntu/.mujoco/mujoco200/'
# sys.path.append("/home/bubuntu/Documents/Val/ML_training/github_repo/venv/lib/python3.6/site-packages/mujoco_py")
print(sys.version)
print(sys.path)

import mujoco_py
print(os.getcwd())
# import mujoco_py
for k, v in os.environ.items():
    if 'mujoco' in v:
        print(k,v)

pdb.set_trace()
env = gym.make("Ant-v3")

env.render()
env.reset()
print("done")