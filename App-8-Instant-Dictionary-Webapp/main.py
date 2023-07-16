from webapp.home import Home
from webapp.about import About

import justpy as jp

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

jp.justpy()
