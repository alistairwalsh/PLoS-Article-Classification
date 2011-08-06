#!/usr/bin/python

import setup, csv, words
from datetime import datetime

s = setup.sample(10000,6000)

print datetime.now(), 'finished gathering sample articles'

csv.writer(open('../data/test_ids.csv','w')).writerow([f['id'] for f in s['test']])
csv.writer(open('../data/train_ids.csv','w')).writerow([f['id'] for f in s['train']])

counter = words.counter([f[setup.__text__][0] for f in s['train'] if len(f[setup.__text__][0]) > 0],
    normalize=True,dictionaryFile='../data/dictionary.csv')
mapper = words.mapper([f[setup.__subject__][0] for f in s['train'] if len(f[setup.__subject__][0]) > 0],
    categoryFile='../data/category.csv')

train = csv.writer(open('../data/train.csv','w'))
test = csv.writer(open('../data/test.csv','w')) 
ytrain = csv.writer(open('../data/ytrain.csv','w')) 
ytest = csv.writer(open('../data/ytest.csv','w')) 

print datetime.now(), 'converting to vectors and storing to csv'
for f in [f[setup.__text__][0] for f in s['train'] if len(f[setup.__text__][0]) > 0]:
    train.writerow(counter.vector(f))
for f in [f[setup.__subject__][0] for f in s['train'] if len(f[setup.__text__][0]) > 0]:
    ytrain.writerow(mapper.vector(f))

for f in [f[setup.__text__][0] for f in s['test'] if len(f[setup.__text__][0]) > 0]:
    test.writerow(counter.vector(f))
for f in [f[setup.__subject__][0] for f in s['test'] if len(f[setup.__text__][0]) > 0]:
    ytest.writerow(mapper.vector(f))

print datetime.now(), 'finished'
