#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author duzy
# @Time      : 2020/3/12 15:58
# @Author    : duzy
# @File      : factoryMode1.py
# @Software  : PyCharm
import xml.etree.ElementTree as etree
import json

class JSONConnector:
    def __init__(self,filepath):
        self.data = dict()
        with open(filepath,mode='r',encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLConnector:
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def connector_factory(filepath):
    if filepath.endwith('json'):
        connector = JSONConnector()
    elif filepath.endwith('xml'):
        connector = XMLConnector()
    else:
        raise ValueError(F'Cannot connect to {filepath}')
    return connector(filepath)

def main():
    pass

