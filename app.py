from flask import Flask , request
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
app = Flask(__name__)

@app.route('/')
def main():
    return 'API is working!'

@app.route('/summary', methods=['GET'])
def summary():
    text= request.args.get('text')
    summarizer(text, max_length=130, min_length=30, do_sample=False)

if __name__ == '__main__':
  app.run()

