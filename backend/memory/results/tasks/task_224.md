# Task 224

**Prompt:** In diesem Code wird `logging`, eine eingebaute Python-Bibliothek, verwendet. Jedes Ereignis (Task-Start, Task-End, Fehler und Warnung) wird mit einem Zeitstempel im Log 'my_app.log' aufgezeichnet. Sie können den Pfad der Log-Datei entsprechend Ihrer Anforderung einstellen. Stellen Sie sicher, dass Ihre Anwendung Schreibzugriff auf das angegebene Verzeichnis hat.

**Result:**
Um dies in Python durchzuführen, benötigen wir die `logging` Bibliothek. Im untenstehenden Code stellen wir das Level unseres Loggers auf `logging.DEBUG` ein, damit alle Nachrichten dieses Levels und höher aufgezeichnet werden. Wir nutzen `logging.basicConfig()`, um festzulegen, dass die Nachrichten in einer Datei namens 'my_app.log' gespeichert werden sollen:

```python
import logging
import time

# Erstellen Sie den Logger und setzen Sie das Level auf DEBUG
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Erstelle einen Handler, der INFO-Nachrichten oder höher an die Protokolldatei schreibt
handler = logging.FileHandler('my_app.log')
handler.setLevel(logging.INFO)

# Erstelle einen Formatter und füge ihn zum Handler hinzu
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Füge den Handler zum Logger hinzu
logger.addHandler(handler)

# Verwende den Logger im Code
logger.info('Task started')
# füge hier ihren Code hinzu...

logger.info('Task ended')

# verwende try/except, um Fehler zu erfassen und zu protokollieren
try:
    # füge fehlerverursachenden Code hier hinzu...
    pass
except Exception as e:
    logger.error('Failed to complete task', exc_info=True)
```

Wir fügen auch ein Format zum Handler hinzu, das einen Zeitstempel vor jeden Log-Eintrag setzt. Dann verwenden wir `logger.info` und `logger.error`, um Ereignisse im Log aufzuzeichnen. `exc_info=True` in `logger.error` sorgt dafür, dass Stacktrace-Informationen aufgezeichnet werden, wenn es einen Fehler gibt. 

Stellen Sie sicher, dass das Verzeichnis, in das Sie protokollieren, existiert und dass Ihre App Schreibzugriff hat.
