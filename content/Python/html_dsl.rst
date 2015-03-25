HTML dsl under python
=====================
:slug: html-dsl-under-python
:tags: python, html, dsl
:date: 2014-08-28 17:00
:category: Python
:author: Andrew V.

Today, after a long process of seeking for dsl under python I've found one interesting `gist <https://gist.github.com/kstep/3360002>`_ on `github <https://github.com>`_ where the `author <https://gist.github.com/kstep/>`_ wrote a little module which provides fast and short describing html-templates and rendering them.

I've analized this code and understood that this snippet doesn't  support working in thread and after some having a think I've realized this feature using threading module. Context information is stored in dictionary, where key-value is formed using thread name-attribute. Module threading supports naming threads with same names and a programmer must be carefull using this code, but in most cases threads are automatically named using template "MainThread,Thread-<1> .... Thread-<N>", so at most it mught be usefull for somebody :)

.. code-include:: html.py
    :lexer: python
    :encoding: utf-8
    :tab-width: 3

There is a few examples of using it:

.. code-include:: test_html.py
    :lexer: python
    :encoding: utf-8
    :tab-width: 3



