from full_writer import autoflow_full_book
from zip_exporter import export_zip

title = "Die Macht des inneren Kindes"
style = "inspirierend"

book = autoflow_full_book(title, style)
path = export_zip(title, book, {"style": style, "autor": "Auto-GPT"})
print("ZIP gespeichert:", path)
