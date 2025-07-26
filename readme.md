# End To End Data Sciende Project

1. create your environment , run command `conda create -p venv python==version`
2. now activate the environment , run command `conda activate venv/`
3. initialize git , run command `git init` and add readme file `git add filename` then commit `git commit -m "first commit"` and select branch `git branch -M main` and check branch `git branch` , now link with github with url `git remote add origin url` and finally puch on github `git push -u origin main`
4. create gitignore file , Go to github and click on **Add file** then click on **create new file** and write `.gitignoe` and choose gitignoe template is **python**
5. if you need .gitignore file from github to your vscode `git pull origin main`
6. now install libraries , to create `requirements.txt` and write libraries names inside **requirements.txt** and run command `pip install -r requirements.txt`
7. create **src folder** and create file `__init__.py`
8. create `setup.py` file on your main root then write codes to setup and run this command `python setup.py install` to make package. **or** write in **-e .** in requirement.txt file and run command `pip install -r requirements.txt`
9. create `template.py` file and write code to make folders and files.
