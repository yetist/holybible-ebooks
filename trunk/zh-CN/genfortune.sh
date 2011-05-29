#!/bin/sh
cat zh-CN.data| while read l;
do
	name=`echo $l|awk '{print $1}'`
	num=`echo $l|awk '{print $2}'`
	cont=`echo $l|cut -d " " -f3-`
	rn=`grep $name zh-CN.inx|awk '{print $3}'`
	echo "$cont 【$rn $num】"
	echo "%"
done 
