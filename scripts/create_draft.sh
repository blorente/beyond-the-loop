#!/bin/bash
set -xe
source scripts/funcs.sh
date=$(date_now)

title=$1
template_path=$2
title_sanitized=$(echo "${title}" | tr " " "-" | tr "[:upper:]" "[:lower:]")

cat "${template_path}" | \
  sed "s/__TITLE__/${title}/g" | \
  sed "s/__TITLE_URL__/${title_sanitized}.html/g" | \
  sed "s/__DATE__/${date}/g" > "_drafts/${date}-${title_sanitized}.md"
