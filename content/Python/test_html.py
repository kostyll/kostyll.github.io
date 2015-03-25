import threading
from Queue import Queue

results = Queue()

from html import *

def layout():
    def head(title, styles=[], scripts=[], meta={}, http={}, prop={}):
        with HEAD:
            TITLE(title)

            for style in styles:
                CSS(style)

            for script in scripts:
                JS(script)

            for name, value in meta:
                META(name=name, content=value)

            for name, value in http:
                META(http_equiv=name, content=value)

            for name, value in prop:
                META(property=name, content=value)

    def field(id, name=None, value=None, label=None, type='text', help=None):
        with DIV.control_group:
            if label is not None:
                LABEL.control_label(label, for_=id)

            with DIV.controls:
                INPUT(id=id, type=type, name=name, value=value)
                if help is not None:
                    P.help_block(help)

    with HTML5:
        head('Page title',
                styles=['http://netdna.bootstrapcdn.com/twitter-bootstrap/2.0.4/css/bootstrap-combined.min.css'],
                scripts=['http://code.jquery.com/jquery.min.js',
                    'http://netdna.bootstrapcdn.com/twitter-bootstrap/2.0.4/js/bootstrap.min.js'])

        with BODY.main:
            with DIV.content(id='content'):
                H1('Hello, world!')

                with FORM('/my-page').well.form_horizontal, FIELDSET:
                    field(id='input01', label='Text input', help='This is a help text.')
                    field(id='input02', label='Checkbox', type='checkbox')

                    with DIV.control_group:
                        LABEL.control_label('Select list', for_='input03')

                        with DIV.controls, SELECT(id='input03'):
                            for option in xrange(1, 9):
                                OPTION(option)

                    with DIV.form_actions:
                        BUTTON(type='submit').btn.btn_primary('Save changes')
                        BUTTON.btn('Cancel')


def layout1():
    with HTML5:
        with HEAD:
            TITLE("title 1")

        with BODY.main:
            H1("HEllo !!! layout1")


def layout2():
    with HTML:
        with BODY.main:
            H2("Hello !!! layOUT 2 !!!")


def thread_worker(layout_renderer):

    layout_renderer ()
    result = str(context)
    # print (result)
    results.put(result)


def main():

    layout()
    print(context)

    thread1 = threading.Thread(target=thread_worker,args=(layout1,))
    thread2 = threading.Thread(target=thread_worker,args=(layout2,))

    threads = (thread1,thread2)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    while not results.empty():
        item = results.get()
        print ("****************")
        try:
            print (item['data'])
        except:
            print (item)

if __name__ == "__main__":
    main()
