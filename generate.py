from model import TextGenerator
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='model.pkl')
parser.add_argument('--prefix', default=None)
parser.add_argument('--length', default=10)
arguments = parser.parse_args()

with open(arguments.model, 'rb') as f:
    text_model = pickle.load(f)
    text_model.generate(int(arguments.length), arguments.prefix)
