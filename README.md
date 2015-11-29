# i18n
Project internationalization strategies for Python

Translating a project is not an easy task. Before even getting into language and cultural issues, there's a huge amount of work involved into the infrastructure needed to make your messages easily replaceable for equivalent strings.

Right now, the best approach for Python projects seems to be [gettext](https://docs.python.org/3.4/library/gettext.html). It relies on Linux gettext infrastructure, which means the need to create .po and .mo files.

I found out that the following steps are required in order to create a proper infrastructure:

1) Create a python file like this:

    :::python
    import gettext
    gettext.gettext('this')
    
2) Run the following command under linux:

    :::bash
    sudo apt-get install gettext  #if you don't have it yet
    xgettext --from-code=UTF-8 -o messages.pot *.py

This will generate a messages.pot file that contains a translation template.
    
3) Open that pot file in a translation editor like [Lokalize](https://userbase.kde.org/Lokalize)

4) Add some translations:

    msgid "this"     #original message
    msgstr "isso"    #translation

5) Save it as a translation (.po) file.

6) Compile it into a mo file:

    :::bash
    msgfmt messages.po -o messages.mo

7) Place the generated .mo file into your localized messages folder. Mine was: (project env)/share/locale/pt_BR/LC_MESSAGES

Simple! (not even close!)

I'll try to create a better way to do it and add it to this repository. 

Wish me luck!

    
    
