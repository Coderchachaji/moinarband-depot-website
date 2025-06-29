from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Function to scan templates folder and get all HTML files
def get_html_files():
    html_files = []
    templates_path = os.path.join(app.root_path, "templates")
    for file in os.listdir(templates_path):
        if file.endswith(".html") and file != "index.html":  # Exclude the main index page
            html_files.append(file)
    return html_files

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = request.form.get("search", "").lower()
    all_files = get_html_files()
    # Filter links based on search query
    filtered_links = [file for file in all_files if search_query in file.lower()] if search_query else all_files
    return render_template("index.html", links=filtered_links)

# Create a route for each HTML file dynamically
@app.route("/<filename>")
def serve_page(filename):
    return render_template(f"{filename}")

if __name__ == "__main__":
    app.run(debug=True)
