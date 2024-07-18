import json

from datasets import load_dataset
from haiku import HaikuDetector
import logging

logging.basicConfig(level=logging.ERROR)
logging.disable(level=logging.ERROR)

ds = load_dataset("statworx/haiku")

raw_haiku = []
for poem in ds['train']['text']:
    lines = poem.split('/')
    raw_haiku.append(lines)

three_line_haiku = []
for h in raw_haiku:
    if len(h) == 3:
        three_line_haiku.append(h)

real_haiku = []
hd = HaikuDetector()
for h in three_line_haiku:
    if hd.is_haiku(h):
        real_haiku.append([x.strip() for x in h])

with open('haiku_list.json', 'w') as f:
    json.dump(real_haiku, f)
