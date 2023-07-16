from webapp import layout, page

import justpy as jp


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        _layout = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=_layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text='This is the home page!', classes='text-4xl m-2')
        jp.Div(a=div, text="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum 
        has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
        type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the 
        leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
        release of sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like 
        Aldus PageMaker including versions of Lorem Ipsum.
        """, classes='text-lg')
        return wp
