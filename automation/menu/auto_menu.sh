#!/bin/bash
select opt in "Workflow starten" "Auto-Review" "Skillmeter" "Exit"; do
  case $opt in
    "Workflow starten") ./tools/auto/auto_task.sh ;;
    "Auto-Review") cat reviews/auto/auto_review.md ;;
    "Skillmeter") cat logs/tagging/auto_tag_skill.log ;;
    "Exit") break ;;
  esac
done
