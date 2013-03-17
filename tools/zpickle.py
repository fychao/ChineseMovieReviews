#!/usr/bin/env python
# -*- coding:utf8 =*-
import zlib, cPickle

def _zdumps(obj):
    return zlib.compress(cPickle.dumps(obj,cPickle.HIGHEST_PROTOCOL),9)

def _zloads(zstr):
    return cPickle.loads(zlib.decompress(zstr))  

def zdumps(obj, fn):
    return open(fn, "w").write(_zdumps(obj)) 

def zloads(fn):
    return _zloads(open(fn, "r").read())
