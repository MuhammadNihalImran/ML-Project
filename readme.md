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
10. go to src folder then `logger.py` file and write the code.
11. In `data_ingestion.py` and get data from **MY SQL** also create **.env** file
12. now go to `utils.py` file and read data and add in requirement.txt file `python-dotenv`,`mysql-connector-python` , `pymysql`, `scikit-learn` to install
13. now install dvc `pip install dvc` and aslo run `dvc init` and then delete folder **artifacts** then now push on github and run `python app.py` then run `dvc add artifacts/raw.csv`.
14. `git checkout` and `git checkout commit_url` and `dvc checkout` and `git checkout main` and `dvc checkout`
15. if you use jupyter notebook in vscode run `pip install ipykernel`
16. In dat_tranformer.py file and code
