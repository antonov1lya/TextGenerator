from model import TextGenerator
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='model.pkl', type=str)
parser.add_argument('--prefix', default=None, type=str, nargs=3)
parser.add_argument('--length', default=10, type=int)
parser.add_argument('--seed', default=None, type=int)
arguments = parser.parse_args()

with open(arguments.model, 'rb') as f:
    text_model = pickle.load(f)
    print(text_model.generate(arguments.length, arguments.prefix, arguments.seed))
