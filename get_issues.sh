#!/bin/sh

page=1

while :
do

	res=$(curl -G\
		-H "Accept: application/vnd.github+json" \
		-d state='all' \
		-d per_page=100 \
		-d page=${page} \
		https://api.github.com/repos/matomo-org/matomo/issues)

	if [[ ${#res} -gt 4 ]]; then
		echo ${res} > matomo-org/matomo/matomo${page}.json
		(( page++ ))
	else
		break
	fi
done
