#!/bin/bash
set -xe
source scripts/funcs.sh
date=$(date_now)

post_path=$1
dest_path=$(echo $post_path | sed 's:_drafts:_posts:' | sed "s:....-..-..:${date}:" ) 
cat "${post_path}" | sed "s/date:.*/date: ${date}/" > ${dest_path}
rm ${post_path}