import json
import random
import openai
import pandas as pd
import speech_recognition as sr
import matplotlib.pyplot as plt
import pyfiglet
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

# 🎨 Cool Console Effects
console = Console()

# 🚀 AI Summaries (Set Your OpenAI API Key)
openai.api_key = "your-openai-api-key"

class LibraryManager:
    def __init__(self):
        self.books = []
        self.storage_file = "books_data.json"
        self.load_books()
        self.show_intro()

    def load_books(self):
        try:
            with open(self.storage_file, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def show_intro(self):
        """🎉 Shock the User with an ASCII Title"""
        title = pyfiglet.figlet_format("LIBRARY MANAGER")
        console.print(f"[bold magenta]{title}[/bold magenta]")

        # ⏰ Time-Based Greetings
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Good morning, Book Lover! ☀️"
        elif current_hour < 18:
            greeting = "Good afternoon, Reader! 📖"
        else:
            greeting = "Good evening, Night Owl! 🌙"

        console.print(f"[cyan]{greeting} Welcome to your Personal Library![/cyan]\n")
    
    def add_book(self):
        """🔥 Add a Book with Achievements"""
        book_title = input("📕 Enter book title: ")
        book_author = input("✍️ Enter author: ")
        book_year = input("📅 Enter publication year: ")
        book_genre = input("🎭 Enter genre: ")
        is_read = input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": book_year,
            "genre": book_genre,
            "read": is_read,
        }

        self.books.append(new_book)
        self.save_books()
        console.print("📚 [green]Book added successfully![/green]")

        # 🎖 Unlock Achievements
        if len(self.books) == 5:
            console.print("🏆 [gold]ACHIEVEMENT UNLOCKED: Book Collector![/gold]")
        elif len(self.books) == 10:
            console.print("🥇 [blue]MASTER LIBRARIAN: You’ve added 10 books![/blue]")

    def view_books(self):
        """📊 View Books in a Fancy Table"""
        if not self.books:
            console.print("❌ [red]No books found![/red]")
            return

        table = Table(title="📚 My Books")
        table.add_column("No.", style="cyan", justify="center")
        table.add_column("Title", style="magenta")
        table.add_column("Author", style="green")
        table.add_column("Year", style="yellow", justify="center")
        table.add_column("Genre", style="blue")
        table.add_column("Status", style="red")

        for index, book in enumerate(self.books, 1):
            table.add_row(
                str(index),
                book["title"],
                book["author"],
                book["year"],
                book["genre"],
                "✅ Read" if book["read"] else "❌ Unread"
            )

        console.print(table)

    def generate_book_summary(self):
        """🤯 AI-Generated Book Summary"""
        book_title = input("🔎 Enter the book title for AI Summary: ")

        console.print("🤖 [cyan]Generating AI summary...[/cyan]")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who gives short book summaries."},
                {"role": "user", "content": f"Give a brief summary of {book_title}."},
            ],
        )
        summary = response["choices"][0]["message"]["content"]
        console.print(f"\n📖 [bold yellow]Summary for {book_title}:[/bold yellow]\n{summary}\n")

    def recommend_books(self):
        """💡 Random Book Recommendations"""
        if not self.books:
            console.print("❌ [red]No books available for recommendations.[/red]")
            return

        recommendations = random.sample(self.books, min(3, len(self.books)))
        console.print("📖 [blue]Recommended Books:[/blue]")
        for book in recommendations:
            console.print(f"  🔹 {book['title']} by {book['author']}")

    def view_reading_progress(self):
        """📊 Show Reading Progress with Animation"""
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book["read"])
        completion_rate = (read_books / total_books * 100) if total_books > 0 else 0

        console.print(f"📖 Total books: {total_books}")
        console.print(f"📊 Reading progress: {completion_rate:.2f}%\n")

        labels = ["Read", "Unread"]
        sizes = [read_books, total_books - read_books]
        colors = ["#4CAF50", "#FF6347"]

        with Progress() as progress:
            task = progress.add_task("📚 Tracking Progress...", total=100)
            while not progress.finished:
                progress.update(task, advance=completion_rate)
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
        plt.title("📊 Reading Progress")
        plt.show()

    def voice_add_book(self):
        """🎤 Add Books with Voice Input"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            console.print("🎤 [cyan]Say the book title...[/cyan]")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            book_title = recognizer.recognize_google(audio)
            console.print(f"✅ You said: [bold yellow]{book_title}[/bold yellow]")
            book_author = input("Enter author: ")
            self.books.append({"title": book_title, "author": book_author, "year": "Unknown", "genre": "Unknown", "read": False})
            self.save_books()
            console.print("📚 [green]Book added successfully![/green]")
        except (sr.UnknownValueError, sr.RequestError):
            console.print("❌ [red]Voice input failed.[/red]")

    def run(self):
        """🏆 Main Menu"""
        while True:
            console.print("1️⃣ Add Book\n2️⃣ View Books\n3️⃣ AI Summary\n4️⃣ Recommend Books\n5️⃣ Progress\n6️⃣ Voice Add Book\n7️⃣ Exit")
            choice = input("🔷 Choose an option: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.generate_book_summary()
            elif choice == "4":
                self.recommend_books()
            elif choice == "5":
                self.view_reading_progress()
            elif choice == "6":
                self.voice_add_book()
            elif choice == "7":
                break

if __name__ == "__main__":
    LibraryManager().run()


# pip install rich pyfiglet openai pandas speechrecognition matplotlib
