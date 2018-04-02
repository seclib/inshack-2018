#!/usr/bin/env python3
# -!- encoding:utf8 -!-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    file: gen_dna.py
#    date: 2017-09-06
#  author: paul.dautry
# purpose:
#       DNA-encode data
# license:
#       GPLv3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#===============================================================================
# IMPORTS
#===============================================================================
import sys
#===============================================================================
# GLOBALS / CONFIG
#===============================================================================
#===============================================================================
# FUNCTIONS
#===============================================================================
#-------------------------------------------------------------------------------
# b2d 
#-------------------------------------------------------------------------------
def b2d(o):
    dna = ''
    for i in range(0,4):
        v = (o >> ((3-i)*2)) & 3
        if v == 0:
            dna += 'A'
        elif v == 1:
            dna += 'C'
        elif v == 2:
            dna += 'G'
        elif v == 3:
            dna += 'T'
    return dna
#-------------------------------------------------------------------------------
# dna_encode
#-------------------------------------------------------------------------------
def dna_encode(data):
    dna = ''
    for o in data:
        dna += b2d(o)
    dna += b2d(0x00)
    return dna
#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print('usage: %s "<command>"' % sys.argv[0])
        exit(1)
    print('nop (0x90) in DNA is: %s' % b2d(0x90))
    print('encoding: %s' % sys.argv[1])
    print(dna_encode(sys.argv[1].encode('utf-8')))
    exit(0)
#===============================================================================
# SCRIPT
#===============================================================================
if __name__ == '__main__':
    main()