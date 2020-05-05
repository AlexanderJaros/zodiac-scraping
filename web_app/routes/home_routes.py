# zodiac-scraping/routes/home_routes.py

from flask import Blueprint, render_template, redirect, flash, request 
import requests
from app.ssa import ssa_scrape 
from app.zodiac import zodiac_scrape
import os
import json

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html") 

@home_routes.route("/result", methods=["POST"]) #https://www.youtube.com/watch?v=AEM8_4NBU04
def pass_sign():
    sign = request.form["sign"]
    zodiac_output = zodiac_scrape(sign)
    name = request.form["name"]
    sex = request.form["sex"]
    ssa_output = ssa_scrape(name, sex)
    print (ssa_output)
    return render_template("result.html", sign = sign, zodiac_output = zodiac_output, ssa_output = ssa_output, name=name, sex=sex )
