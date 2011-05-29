#! /usr/bin/env python2
# -*- encoding:utf-8 -*-
# FileName: genrst.py

"This file is part of ____"
 
__author__   = "yetist"
__copyright__= "Copyright (C) 2011 yetist <xiaotian.wu@i-soft.com.cn>"
__license__  = """
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
import os

buf = open("zh-CN.inx").read()
cont = open("zh-CN.data").read()

def do_chp(chp):
    match_name = chp[0]
    chp_name = chp[1]
    sht_name = chp[2]
    count = chp[5]
    if match_name == "Gen":
        print "旧约全书"
        print "========="
        print 
    if match_name == "Mat":
        print "新约全书"
        print "========="
        print 
    if len(chp) == 7:
        print "[%s]" % (chp[6])
        print "--------------------"
    print "%s(%s)    计%s章" % (chp_name, sht_name, count)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    for i in cont.splitlines():
        if i.startswith(match_name):
            s = i.split()
            nums = s[1].split(":")
#            if nums[1] == "1":
#                print "%s(%s)" % (sht_name, nums[0])
#                print "~~~~~~~~~~~"
#                print
            print i[i.index(" ")+1:]
            print

def main():
    print "============"
    print "圣 经"
    print "============"
    print 
    print ".. contents:: 目录"
    print 
    for i in buf.splitlines():
        chapter = i.split()
        do_chp(chapter)

if __name__=="__main__":
    main()
