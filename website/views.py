from flask import Blueprint, render_template, request, current_app
from flask_login import login_required, current_user
import os
from utils import parse_chat_log, get_statistics, get_keywords, extract_messages, generate_summary

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        file = request.files.get('chatfile')
        if file and file.filename.endswith('.txt'):
            # Save uploaded file to configured upload folder
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            chat = parse_chat_log(content)
            stats = get_statistics(chat)
            keywords = get_keywords(chat)
            messages = extract_messages(chat)

            # generate_summary expects stats, keywords, and list of messages (strings)
            summary = generate_summary(stats, keywords, messages)

            # Pass all data to template
            return render_template(
                "index.html",
                summary=summary,
                stats=stats,
                keywords=keywords,
                user=current_user
            )
        else:
            # Handle invalid file type
            return render_template(
                "index.html",
                error="Please upload a valid .txt file",
                user=current_user
            )

    # GET request: show empty form
    return render_template("index.html", user=current_user)
