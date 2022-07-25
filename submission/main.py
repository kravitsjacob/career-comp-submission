from datetime import datetime
import asyncio
import os
import random

os.system(f"export PYTHONPATH={os.getcwd()}")

from dragg_comp.player import PlayerHome
from submission import predict, my_reward

class PlayerSubmission(PlayerHome):
	def __init__(self):
		super().__init__()

	def get_reward(self):
		# redefines get_reward with the player's implementation
		reward = my_reward(self)
		return reward

if __name__=="__main__":
	tic = datetime.now()
	env = PlayerSubmission()

	for _ in range(env.num_timesteps * env.home.dt):
	    action = predict(env)
	    env.step(action) 

	asyncio.run(env.post_status("done"))
	toc = datetime.now()
	print(toc-tic)