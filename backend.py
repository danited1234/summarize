from flask import Flask, request, jsonify
from summarization.summarization import summarize
from flask_cors import CORS


app = Flask(__name__)
CORS(app,resources={r"/upload":{"origins":"http://localhost:3000/"}})


@app.route('/summarize', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return 'No PDF file found', 400

    pdf_file = request.files['pdf']
    # Process the PDF file as needed (e.g., save to disk, manipulate, etc.)
    summary = summarize.ai_summarize(pdf_file)
    data = {"summary":summary}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
