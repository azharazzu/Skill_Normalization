import numpy as np
import pandas as pd
import time
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")
import torch

Data_path = "../Data"
data = os.join.path(Data_path, "training_data.csv")

import logging
from simpletransformers.seq2seq import (Seq2SeqModel, Seq2SeqArgs)
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

cuda_available = torch.cuda.is_available()
print(cuda_available)

def count_matches(labels, preds):
    print(labels)
    print(preds)
    return sum(
        [
            1 if label == pred else 0
            for label, pred in zip(labels, preds)
        ]
    )


model_args = Seq2SeqArgs()
model_args.num_train_epochs = 20
model_args.train_batch_size=32
model_args.no_save = False
model_args.evaluate_generated_text = True
model_args.evaluate_during_training = True
model_args.evaluate_during_training_verbose = True
model_args.use_multiprocessing=False
model_args.overwrite_output_dir=True
model_args.save_model_every_epoch=False
model_args.thread_count=16
model_args.n_gpu=1

model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="facebook/bart-base",
    args=model_args,
    use_cuda=cuda_available,
)

df = pd.read_csv(data, encoding='unicode_escape')
df.dropna(inplace = True)
df.drop(['Flag'],axis=1,inplace=True)
df = df.sample(frac = 1)
df.reset_index(inplace = True, drop = True)

train_df = df.iloc[:64000]
eval_df = df.iloc[64000:]
model.train_model(train_df, eval_data = eval_df, matches=count_matches)
