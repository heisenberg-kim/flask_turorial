from flask import Flask, request, render_template, make_response

app = Flask('ky')

@app.route('/<text>')
def example(text):
	return make_response(render_template('app.html', text = text), 200, {'Content-Type': 'text/html'})

app.run(host='0.0.0.0', port=5001, debug=True)
