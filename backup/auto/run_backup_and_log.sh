#!/bin/bash
./backup/auto/auto_backup.sh && echo "Backup abgeschlossen: $(date)" >> backup/auto/logs/backup_log.md
