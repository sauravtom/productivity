#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib

curr_path = os.path.abspath(__file__)
curr_path = "/".join(curr_path.split('/')[:-1])

hosts_path = '/etc/hosts'
temp_path = '%s/template.txt'%curr_path

def main():
	tmp = open(temp_path).read()
	with open(hosts_path, "w") as f:
	    f.write(tmp)

if __name__ == '__main__':
	main()
