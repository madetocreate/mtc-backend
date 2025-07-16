#!/bin/bash
echo "TEST: Starte alle Automationen..."
./scripts/auto/auto_master.sh
ls -lh backup/auto/ | grep .tar.gz
tail -n 5 logs/auto/global_automation.log

