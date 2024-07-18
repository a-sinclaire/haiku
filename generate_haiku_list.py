import json

from profanity_check import predict
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

clean_haiku = []
for h in real_haiku:
    predictions = predict(h)
    if max(predictions) == 0:
        clean_haiku.append(h)

print(f'{len(clean_haiku)} / {len(raw_haiku)}')

with open('haiku_list.json', 'w') as f:
    json.dump(clean_haiku, f)
