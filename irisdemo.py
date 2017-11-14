#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:53:54 2017

@author: Kirans
"""

from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("keys of iris_dataset: \n{}" .format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193] +"\n..")

print("Target names:{}" .format(iris_dataset['target_names']))

print("First five rows of data:\n{}" .format(iris_dataset['data'][:10]))
