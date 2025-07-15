from full_writer import autoflow_full_book
from exporter import export_txt

title = "Die Macht des inneren Kindes"
style = "inspirierend"

book = autoflow_full_book(title, style)
path = export_txt(title, book)
print("Buch gespeichert:", path)
