import os
import json
from flask import Flask,render_template,abort
app=Flask(__name__)
class Files(object): 
    directory=os.path.join(os.path.abspath(os.path.dirname(__name__)),"..","files")
    def __init__(self):
        self._files=self._get_all_files()
    def _get_all_files(self):
        result={}
        for filename in os.listdir(self.directory):
            filepath=os.path.join(self.directory,filename)
            with open(filepath) as f:
                result[filename[:-5]]=json.load(f)
        return result
    def get_title_list(self):
        return [item['title'] for item in self._files.values()]
    def get_by_filename(self,filename):
        return self._files.get(filename)
files=Files()
@app.route('/')
def index():
    return render_template("index.html",title_list=files.get_title_list())
@app.route('/files/<filename>')
def file(filename):
    file_item=files.get_by_filename(filename)
    if not file_item:
        abort(404)
    return  render_template("file.html",file_item=file_item)
@app.errorhandler(404)
def NOT_FOUND(error):
    return render_template("404.html"),404
if __name__=='__main__':
    app.run()
