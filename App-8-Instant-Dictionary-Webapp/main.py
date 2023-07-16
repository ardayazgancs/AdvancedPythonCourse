from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

import justpy as jp

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
