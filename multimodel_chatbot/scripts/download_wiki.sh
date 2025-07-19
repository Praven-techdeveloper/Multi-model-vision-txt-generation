#!/usr/bin/env bash
set -e
mkdir -p data/wiki
cd data/wiki
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2