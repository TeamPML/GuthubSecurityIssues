#!/bin/sh

# load all both open and closed issues and save as json files
# 100 issues per page, one page == one json file

page=1

while :
do

	res=$(curl -G\
		-H "Accept: application/vnd.github+json" \
		-d state='all' \
		-d per_page=100 \
		-d page=${page} \
		https://api.github.com/repos/$1/issues)

	if [[ ${#res} -gt 4 ]]; then
		echo ${res} > ../data/$1/${page}.json
		(( page++ ))
	else
		break
	fi
done
