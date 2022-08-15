#!/usr/bin/bash

echo Starting stage 1
python3 build_stage1.py

echo Starting stage 2
python3 build_stage2.py

rm user_anime_list_df_pivot.pkl