```python
# modules/content/bookbot.py

# Import necessary libraries and modules
from gpt4o import GPT4o
from memory import Memory
from format_templates import MarkdownTemplate

class BookBot:
    def __init__(self):
        # Initialize GPT-4o model for text generation and editing
        self.gpt4o = GPT4o()
        # Initialize Memory for storing user interactions and drafts
        self.memory = Memory()
        # Initialize MarkdownTemplate for formatting the book content
        self.md_template = MarkdownTemplate()

    def write_book(self, title, outline):
        """
        Generates book content based on the given title and outline.
        
        :param title: Title of the book
        :param outline: Detailed outline of chapters and sections
        :return: Generated book content as Markdown
        """
        # Store initial request in memory
        self.memory.store_request('write_book', {'title': title, 'outline': outline})
        
        # Generate content for each section in the outline
        book_content = ''
        for chapter, sections in outline.items():
            chapter_content = f'# {chapter}\n'
            for section in sections:
                section_content = self.gpt4o.generate_text(f"{section} in context of {title}")
                chapter_content += f"## {section}\n{section_content}\n"
            book_content += chapter_content
        
        # Format the book content as Markdown
        formatted_content = self.md_template.apply(book_content)
        
        # Store generated content in memory
        self.memory.store_generated_content('book_content', formatted_content)
        
        return formatted_content

    def edit_book(self, book_content):
        """
        Edits the given book content for grammatical correctness and style.
        
        :param book_content: The raw book content to be edited
        :return: Edited book content as Markdown
        """
        # Store initial content before editing in memory
        self.memory.store_request('edit_book', {'content': book_content})
        
        # Use GPT-4o to edit and improve the book content
        edited_content = self.gpt4o.edit_text(book_content)
        
        # Store edited content in memory
        self.memory.store_generated_content('edited_book_content', edited_content)
        
        return edited_content

# Example usage:
# book_bot = BookBot()
# outline = {
#     "Introduction": ["The Purpose of the Book", "How to Use This Book"],
#     "Chapter 1: Getting Started": ["Understanding the Basics", "First Steps"],
# }
# generated_book = book_bot.write_book("The Journey of Writing", outline)
# edited_book = book_bot.edit_book(generated_book)
```