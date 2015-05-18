Command line JSON parser via jq
###############################

:date: 2013-10-14 22:30
:tags: unix
:category: misc
:slug: command-line-json-parser-via-jq
:summary: jq: a command line json parser


A command-line JSON parser can be handy when you test or debug JSON web
services. Unfortunately inspecting JSON responses via command line are hard to
read and not easy to manipulate with traditional Unix utilities.

Today I stumbled on `jq <http://stedolan.github.io/jq/>`_, via `Angel Ramboi
<https://github.com/limpangel>`_. ``jq`` is a lightweight and flexible
command-line JSON processor.

Download the desired binary and then ``chmod +x ./jq``.

I've prepared a sample json so we can see how easily it is to inspect and
manipulate JSON strings.


.. sourcecode:: python

    >> cat sample.json

    {
        "first": "John",
        "last": "Doe",
        "age": 27,
        "sex": "M",
        "registered": true,
        "interests": [ "Reading", "Mountain Biking", "Hacking" ],
        "favorites": {
            "color": "Blue",
            "sport": "Soccer",
            "food": "Spaghetti"
        },
        "skills": [
            {
                "category": "Python",
                "tests": [
                    { "name": "One", "score": 90 },
                    { "name": "Two", "score": 96 }
                ]
            },
            {
                "category": "GO",
                "tests": [
                    { "name": "One", "score": 32 },
                    { "name": "Two", "score": 84 }
                ]
            }
        ]
    }



Simple filtering:


.. sourcecode:: python

    >> cat sample.json | jq '.skills[].category'

    Python
    Go


Filtering with index:


.. sourcecode:: python

    >> cat sample.json | ./jq '.["skills"][0]["tests"][1] | .name, .score'

    "Two"
    96


...or a different flavour:


.. sourcecode:: python

    >> cat sample.json | ./jq '.skills[0].tests[1] | .name, .score'

    "Two"
    96


Built-in operators:


.. sourcecode:: python

    >> cat sample.json | ./jq '.interests | length' 

    3


Manipulate JSON string:


.. sourcecode:: python

    >> cat sample.json | ./jq 'if .registered == true then .skills[].tests[].score = 1000 else null end' > new_sample.json


Head on and read the `jq manual <http://stedolan.github.io/jq/manual/>`_ if you
want to include it in your tester toolbox.
