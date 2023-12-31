from webapp import layout, page

import requests
import justpy as jp


class Dictionary(page.Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        _layout = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=_layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')
        jp.Div(a=div, text='Get the definition of any English word instantly as you type.', classes='text-lg')

        input_div = jp.Div(a=div, classes='grid grid-cols-2')

        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border border-blue-500 h-40')
        input_box = jp.Input(a=input_div, placeholder='Type in a word here...', outputdiv=output_div,
                             classes='m-2 bg-gray-100 border border-gray-500 rounded w-64 focus:bg-white '
                                     'focus:outline-none focus:border-purple-500 py-2 px-4')
        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        request = requests.get(f'http://127.0.0.1:8000/api?w={widget.value}')
        data = request.json()

        widget.outputdiv.text = ' '.join(data['definition'])
