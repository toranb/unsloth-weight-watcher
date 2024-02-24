import weightwatcher as ww
import matplotlib.pyplot as plt
import pandas as pd

watcher = ww.WeightWatcher()
details = watcher.analyze(model='model',fix_fingers='clip_xmax')
base_details = watcher.analyze(model='base',fix_fingers='clip_xmax')

print(details.alpha.mean())
print(base_details.alpha.mean())
details.to_csv('finetune.csv', index=False)
base_details.to_csv('base_data.csv', index=False)

details.alpha.plot.hist(bins=100, color='red', alpha=0.5, density=True, label='finetune')
base_details.alpha.plot.hist(bins=100, color='green', density=True, label='mistral')
plt.legend()
plt.xlabel(r"alpha $(\alpha)$ PL exponent")
plt.title(r"Mistral fine tune layer alphas $(\alpha)$")
plt.savefig("alphas.png")
