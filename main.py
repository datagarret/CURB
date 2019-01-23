from flask import render_template, url_for, Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modules')
def modules():

    modules = [
    {
        'title': 'Module 1',
        'topic': 'Introduction to CURB',
        'id':1
    },
    {
        'title': 'Module 2',
        'topic': 'Going Outside In',
        'id':2
    },
    {
        'title': 'Module 3',
        'topic': 'Habits, Acting & Traps',
        'id':3
    },
    {
        'title': 'Module 4',
        'topic': 'Choosing To Get Back On Track',
        'id':4
    },
    {
        'title': 'Module 5',
        'topic': 'Freedom From Negative Thoughts',
        'id':5
    },
    {
        'title': 'Module 6',
        'topic': 'Changing Your Thoughts and Feelings',
        'id':6
    },
    {
        'title': 'Module 7',
        'topic': 'How to Figure Out What Bothers You',
        'id':7
    },
    {
        'title': 'Module 8',
        'topic': 'Problem Solving In Stressful Situations',
        'id':8
    },
    {
        'title': 'Module 9',
        'topic': 'Relationship Skills Training',
        'id':9
    },
    {
        'title': 'Module 10',
        'topic': 'How Do I Communicate?',
        'id':10
    },
    {
        'title': 'Module 11',
        'topic': 'Relationship Conflicts',
        'id':11
    },
    {
        'title': 'Module 12',
        'topic': 'Dealing With New Life Situations',
        'id':12
    },
    {
        'title': 'Module 13',
        'topic': 'Building a Resilient Life',
        'id':13
    },
    {
        'title': 'Module 14',
        'topic': 'What to Do If You Can\'t Shake the Blues',
        'id':14
    },
]
    return render_template('modules.html', modules=modules, title='Modules')

@app.route('/modules/<int:module_id>')
@app.route('/modules/<int:module_id>/<int:module_part>')
def get_module(module_id, module_part=1):

    #number of current modules in
    module_part_dict = {1:27, 2:12, 3:18, 4:15, 5:16, 6:10, 7:25, 8:16,
                        9:23, 10:18, 11:24, 12:22, 13:20, 14:20}

    module_max = module_part_dict[module_id]


    if module_part - 1 > 0:
        last_url = url_for('get_module',
                           module_id= module_id,
                           module_part=module_part - 1)
    else:
        last_url = None

    if module_part + 1 <= module_max:
        next_url = url_for('get_module',
                            module_id=module_id,
                            module_part=module_part + 1)
    else:
        next_url = None

    mod_curr = 'modules/module{}/module{}_{:02d}.html'.format(module_id, module_id, module_part)

    percent_complete = ":.1%".format(module_part/module_max)

    return render_template(mod_curr, module_id=module_id, module_part=module_part,
                           last_url=last_url, next_url=next_url, module_max=module_max)



@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQ')


@app.route('/roadblocks')
def roadblocks():
    return render_template('roadblocks.html', title='Road Blocks')

@app.route('/feeling')
def feeling():
    return render_template('feeling.html', title='I am Feeling...')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
