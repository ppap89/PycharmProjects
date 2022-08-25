import os
import numpy as np
import ffmpeg

from multiprocessing.dummy import Pool as ThreadPool

path = 'G:/observer_compute_intelligence/data/youtubedl/video/parking'

def count_duration(path):
    files = []
    for r, ds, fs in os.walk(path):
        for f in fs:
            if f.lower().endswith('mp4'):
                file = os.path.join(r, f)
                files.append(file)

    p = ThreadPool()
    ret = p.map(lambda file: float(
        ffmpeg.probe(file)['format']['duration']), files)
    p.close()
    p.join()

    return(np.sum(ret) / 60 / 60)


dirs = [os.path.join(path, d) for d in os.listdir(path)]

for d in dirs:
    if os.path.isdir(d):
        t = count_duration(d)
        print(f'[{d}] \t=>\t [{t}]'.format(d, t))
