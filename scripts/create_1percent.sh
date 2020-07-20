#!/bin/bash
set -xe

title=$1
title_sanitized=$(echo "${title}" | tr " " "-" | tr "[:upper:]" "[:lower:]")
date=$(printf '%(%Y-%m-%d)T\n' -1)

cat ./scripts/1_percent_template | \
  sed "s:__TITLE__:${title}:g" | \
  sed "s:__TITLE_URL__:${title_sanitized}.html:g" | \
  sed "s:__DATE__:${date}:g" > "_drafts/${date}-${title_sanitized}.md"
