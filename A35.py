# DSML Advanced: Probability and Statistics - 1
###################################################
######### Reference links #########
# https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video_galleries/video-lectures/
####################################################

## Coin toss
# Plot probability of occurrence of head when a coin is tossed(by default it a fair coin,i.e,p_h=p_t=0.5) as the number of trails/tosses increases.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

class CoinTossSequence:
  def __init__(self, p_h=0.5, num_tosses=100): #p_h is probability of getting heads as outcome
    self.p_h = p_h
    self.num_tosses = num_tosses
    self.animate_coin_toss_sequence()

  def toss_coin(self):
    all_tosses = []
    cumulative = [0]  #array to store probabilities of head occurrences 
    for toss_id in range(self.num_tosses):
      toss_value = np.random.choice(a=[0,1],p=[1-self.p_h,self.p_h])
      all_tosses.append(toss_value)
      cumulative.append(cumulative[toss_id]+toss_value)
    cumulative = cumulative[1:]
    cumulative = [val/(i+1) for i,val in enumerate(cumulative)]
    return np.array(all_tosses), np.array(cumulative)
  
  def animate_coin_toss_sequence(self):
    artists = []
    fig, ax = plt.subplots()
    ax.set_ylim(0,1)
    all_tosses, cumulative = self.toss_coin()
    for i,_ in enumerate(cumulative):
      c = cumulative[0:i]
      line = plt.plot(c,c="c")
      hline = ax.axhline(y=self.p_h,c="y",ls="--")
      artists.append([line[0],hline])
    anim = ArtistAnimation(fig,artists)
    anim.save("coin.gif",fps=10)

if __name__ == "__main__":
  coin = CoinTossSequence()
