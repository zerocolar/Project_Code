__author__ = 'zerocolar'
import pdb
import os
import sys
import random
import math
import dataparse
import numpy

class BaseLearner(object):
    def __init__(self,unlabeled_datasets=None,models=None,undersample_before_eval=False):
        if isinstance(unlabeled_datasets,dataparse.Dataset):
            unlabeled_datasets=[unlabeled_datasets]
        self.unlabeled_datasets = unlabeled_datasets or []
        self.labeled_datasets = [dataparse.Dataset(name=d.name) for d in unlabeled_datasets]
        self.models = models
        self.undersample_before_eval=undersample_before_eval
        self.undersample_function = self.undersample_labeled_datasets
        self.query_function = self.base_q_function
        self.name = "Base"
        self.description = ""
    def active_learn(self,num_examples_to_label,batch_size=5):
        labeled_so_far=0
        while labeled_so_far<num_examples_to_label:
            example_ids_to_label = self.query_function(batch_size)
            if example_ids_to_label:


    def predict(self,X):
        return self.majority_predict(X)
    def majority_predict(self,X):
        votes=[]
        if self.models and len(self.models)>0:
            for m,x in zip(self.models,X):
                votes.append(m.predict(x))
            vote_set=list(set(votes))
            count_in_list = lambda x:votes.count(x)
            return vote_set[_arg_max(vote_set,count_in_list)]
        else:
            return Exception, "No models have been initialized"
    def base_q_function(self,k):
        raise Exception, "no query function provided"
    de
