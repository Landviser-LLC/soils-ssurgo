# soils-ssurgo - to work SmartRice

Planning this SSURGO repo. This is a learning repo on basics of Git, Python, Virtual Environments, Spatial Data, ArcGIS, QGIS, webmaps.

## Beginner: clone and contribute to this repo

`git clone `

Need to setup venv (Python 3.9) - previous Python version, as 3.10 does not support Pandas in a full might yet (June 2022).

`py -m virtualenv -p="[PATH to your Python 3.9]" "[PATH-to-your-repo-folder]\soils-ssurgo\.venv39"`

activate environment
`.venv39/scripts/activate`

install requirements from requirements.txt
`pip install -r requirements.txt`

create your branch

`git checkout -b mywork`

Do coding/data prep work as assigned in Landviser.XYZ portal (eventually we might utilize Issues and Projects tabs here to work on GIS analytic and soft development projects. When finished one task - PUSH to repo and submit pull request.

When pushing a branch first time

`git push --set-upstream origin mywork`

after that you can just

`git push origin`

and changes from local will be pushed to YOUR branch on remote (GitHub, this repo). When finished with an assignment - submit PULL request here on GitHub. Someone from the team will jump in and review/approve/merge.
That will merge your changes to the MASTER and your branch will be deleted.
For the next task always pull fresh copy from the GitHub repo MASTER branch
`git pull origin`
create another branch from master and repeat the above

**REMEMBER:**

* commit and push often, at least at the end of the day! - for safekeeping of your work
* submit PULL request when finished the step in development/data prep

## Repo Structure

**SSURGO** # folder structure of soil data per county downloaded and unzipped (in Future - move the prelim downloaded and unzipped data to the cloud (there is a limit to GitHub repo size) - GDrive, A2 PostgreSQL, doing download/unzip/process on the fly?, paid solution?)

**data_in**  #client data and sample report/workflows

**data_out** #intermediate files as a result of scripts in this repo

**py**  #python code and Jupyter Notebooks

**references** # supplemental information about SSURGO dbase

### TODO:

* [ ] download and extract SSURGO files per county - write JP notebook in **py/**
* [ ] how to put those to GDrive?

* [ ] script to extract and summarize soil properties to mukey - multilevel weighted everages
* [ ] combine several counties spatial/tabular
* [ ] merge spatial/tabular
* [ ] push layer to AGOL (how to use ArcGIS Pro env?) / create REST API at our hosting?


## Advanced How To: Starting from Scratch on new coding project

1. setting up venv for specific Python version:
   `py -0`       #lists all Pythons on Windows PC

Need to setup venv (Python 3.9) - previous Python version, as 3.10 does not support Pandas in a full might yet (June 2022).

`py -m virtualenv -p="C:\Python\py39\python.exe" "C:\c_repos\soils-ssurgo\.venv39"`

2. Activate the environment and install modules
   `.venv39/scripts/activate`

   `pip install pandas`
3. Create .gitignore and add path to venv there (i.e. type there ".venv39")
4. Create requirements.txt for this repo with the enviroment packages installed

`python freeze > requirements.txt`
