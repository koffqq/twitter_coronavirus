#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# import matlap
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['Noto Sans CJK', 'DejaVu Sans','sans-serif']

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# import matlap
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.font_manager as fm
#plt.rcParams['font.family'] = ['Noto Sans CJK', 'DejaVu Sans'] 

# top 10
items_top = sorted(items[:10], key=lambda x: x[1], reverse = False)
x,y = zip(*items_top)
print(x,y)

# English or Korean
if args.input_path == "reduced.country":
    category = "country"
else:
    category = "language"

if args.key == "#coronavirus":
    language = "English"
else:
    language = "Korean"

# plot

plt.bar(range(len(x)), y, color = "blue", width = 0.5)
#print(x, len(x), range(len(x)))
plt.xticks(range(len(x)),x)
#plt.xticklabels(x)
plt.xlabel(category)
plt.ylabel("Count of Tweets")
plt.title("Number of " + language + " Tweet including " + args.key + " in " + category)
#plt.legend()

plt.savefig(f"{language}_{category}.png")

#plt.show()
#try:
 #   plt.savefig(f"{language}_{category}.png")
#except:
 #   print("error")

# The horizontal axis of the graph should be the keys of the input file, only need to include the top 10 keys.
# display Korean
# print(matplotlib.matplotlib_fname())
