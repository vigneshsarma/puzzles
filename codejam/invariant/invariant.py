#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 vignesh <vignesh@vignesh-desktop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       


numbers={6174:0}
sort_num=[]

def find_num_of_iter(val):
	if numbers.has_key(val):
		return numbers[val]
		
	st_val=`val`
	
	if len(st_val)!=4:
		st_val='0'+st_val
	if st_val==st_val[0]+st_val[0]+st_val[0]+st_val[0]:
		return '~'
	
	as_val=int(''.join(sorted(st_val)))
	ds_val=int(''.join(sorted(st_val,reverse=True)))
	
	#print as_val,ds_val,nval
	#raw_input('>>')
	if as_val > ds_val :
		nval=as_val-ds_val
	else : nval=ds_val - as_val
	#print as_val,ds_val,nval
	#raw_input('>>')
	if numbers.has_key(nval):
		itr = numbers[nval]
	else:
		itr=find_num_of_iter(nval)
	itr+=1
	numbers[val]=itr
	return itr


def main():
	

	#if not numbers.has_key(val):
	#val=1000
	for i in range(0,8):
		sort_num.append(0)
	for val in range(1000,9998):
		itr=find_num_of_iter(val)
		print val,': ',itr
		if itr!='~':
			sort_num[itr]+=1
	
	for i in range(0,8):
		print i,': ',sort_num[i]
	

if __name__ == '__main__':
	main()

