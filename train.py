from model import TextGenerator
import argparse
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', default=None, type=str)
parser.add_argument('--model', default='model.pkl', type=str)
arguments = parser.parse_args()

text_model = TextGenerator()
text_model.fit(arguments.input_dir)

with open(arguments.model, 'wb') as f:
    pickle.dump(text_model, f)
