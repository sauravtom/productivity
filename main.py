#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib

curr_path = os.path.abspath(__file__)
curr_path = "/".join(curr_path.split('/')[:-1])

hosts_file = '/etc/hosts'
temp_file = '%s/template.txt'%curr_path

def main():
	master_file = open(temp_file)
	a = master_file.read()
	with open(hosts_file, "w") as f:
	    f.write(a)

if __name__ == '__main__':
	main()
