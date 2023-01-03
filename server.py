from bottle import Bottle, template,request 

app = Bottle()

@app.route('/', method="POST")
def formhandler():
    name = request.forms.get('name')
    id = request.forms.get('identity')
    date = request.forms.get('date')
    mark = request.forms.get('mark')
    kind = request.forms.get('kind')
    desc = request.forms.get('description')
    categ = request.forms.get('category')

    return name,id,date,mark,kind,desc,categ

print(formhandler())

