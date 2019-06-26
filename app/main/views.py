from . import main
from flask import render_template, request, redirect,url_for
from ..requests import get_sources, get_headlines

@main.route('/')
def index():
    sports = get_sources('sports')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    headlines = get_headlines('15')
    business = get_sources('business')
    general = get_sources('general')
    title = 'Newshighlights'
    return render_template('index.html', title = title, sports =sports, entertainment=entertainment, technology=technology, headlines=headlines, business=business, general=general)

@main.route('/source/<string:id>&<int:page_size>')
def get_articles(id,page_size):

    articles = get_source(id,page_size)
    return render_template('articles.html',articles=articles)

@main.route('/source')
def source():
    sports = get_sources('sports')
    entertainment = get_sources('entertainment')
    technology = get_sources('technology')
    business = get_sources('business')
    general = get_sources('general')
    title = 'Newshighlights'
    return render_template('navbar.html', title = title, sports =sports, entertainment=entertainment, technology=technology,business=business, general=general)


