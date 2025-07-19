#!/usr/bin/env bash
set -e
mkdir -p data/wiki_extracted
wikiextractor \
  --infile data/wiki/enwiki-latest-pages-articles.xml.bz2 \
  --outdir data/wiki_extracted \
  --json \
  --no-templates \
  --min_text_length 200