# Task 454

**Prompt:** 4. Benennen Sie Variablen und Funktionen sinnvoll: Die Namen von Variablen und Funktionen sollten ihre Funktion und Verwendung klar hervorheben. Vermeiden Sie es, generische oder unklare Namen zu verwenden.

**Result:**
Hier sind einige Richtlinien, wie Sie Variablen und Funktionen sinnvoll benennen können:

1. **Beschreibende Namen**: Die Namen von Variablen und Funktionen sollten klare Hinweise auf ihren Zweck und ihre Verwendung geben. Zum Beispiel ist `salaries` eine bessere Wahl als `s` für ein Array, das Gehälter enthält.

2. **Verwendung von CamelCase**: In vielen Programmiersprachen ist es üblich, Variablen und Funktionen in CamelCase zu schreiben. Hierbei beginnt das erste Wort klein, und jedes nachfolgende Wort beginnt mit einem Großbuchstaben, wie z. B. `calculateAverageSalary`.

3. **Funktionsnamen sollten Verben sein**: Da Funktionen Aktionen durchführen, sollten sie normalerweise mit Verben benannt werden. Zum Beispiel wäre `calculateTotal` oder `addEmployee` geeignete Funktionsnamen.

4. **Vermeidung von Abkürzungen**: Abkürzungen können verwirrend sein und es erschweren, den Code zu verstehen. Daher ist es besser, vollständige und aussagekräftige Namen zu verwenden.

5. **Konsistente Terminologie**: Innerhalb eines Projekts sollte die Namensgebung konsistent sein. Wenn Sie zum Beispiel `employee` für individuelle Mitarbeiter verwenden, sollten Sie nicht an anderer Stelle `worker` oder `staff` verwenden.

6. **Vermeidung von magischen Zahlen**: Anstatt im Code zufällige Zahlen zu verwenden, ist es besser, eine Variable mit einem beschreibenden Namen zu erstellen. Anstatt also `salary * 0.07` zu schreiben, könnten Sie eine Variable `taxRate` erstellen und `salary * taxRate` schreiben.

7. **Vermeidung von booleschen Variablennamen mit "is" oder "has"**: Für Booleans ist es praktisch, sie mit "is" oder "has" zu beginnen, um klarzustellen, dass sie einen wahren oder falschen Wert haben. Zum Beispiel `isValid` oder `hasPaid`.

8. **Verwenden von Einzahl und Mehrzahl**: Für Sammlungen ist es sinnvoll, Mehrzahl-Namen zu verwenden, z.B. `employees` für eine Liste von Mitarbeitern.

Insgesamt ist das Ziel, den Code so klar und verständlich wie möglich zu machen, damit andere Entwickler (und Sie selbst in der Zukunft) ihn leichter verstehen können.
