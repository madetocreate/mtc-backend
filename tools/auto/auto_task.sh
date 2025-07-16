#!/bin/bash
echo "Tagging und Skillmeter laufen..."
python3 memory/tools/auto_tagger.py
python3 memory/tools/skill_meter.py
