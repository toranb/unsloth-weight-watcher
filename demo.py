import weightwatcher as ww

watcher = ww.WeightWatcher()
details = watcher.analyze(model='model', savefig='yolo')
details.alpha.plot.hist()
