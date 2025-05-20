from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
import datetime
import math

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)

