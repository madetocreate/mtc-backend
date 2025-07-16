def route_task(task): return "buchprojekt_nlp" if "NLP" in task else "uncategorized"
import re

def detect_project(task):
    if "NLP" in task: return "buchprojekt_nlp"
    if "Thriller" in task: return "buchprojekt_thriller"
    if "Roman" in task: return "buchprojekt_roman"
    return "misc"
