# soils-ssurgo - to work SmartRice

Planning this SSURGO repo. This is a learning repo on basics of Git, Python, Virtual Environments, Spatial Data, ArcGIS, QGIS, webmaps.

## Beginner: clone and contribute to this repo

`git clone `


Need to setup venv (Python 3.9) - previous Python version, as 3.10 does not support Pandas in a full might yet (June 2022).

`py -m virtualenv -p="[PATH to your Python 3.9]" "[PATH-to-your-repo-folder]\soils-ssurgo\.venv39"`

activate environment

create your branch

`git checkout -b mywork`

When finished one task - PUSH to repo and submit pull request.

When pushing a branch first time 

`git push --set-upstream origin mywork`

after that you can just

`git push origin`

and changes from local will be pushed to YOUR branch on remote (GitHub, this repo)

**REMEMBER:** 

* commit and push often, at least at the end of the day! - for safekeeping of your work
*  submit PULL request when finished the step in development/data prep

## Repo Structure

**SSURGO** # folder structure of soil data per county downloaded and unzipped

**data_in**  #client data and sample report/workflows

**py**  #python code and Jupyter Notebooks

**references** # supplemental information about SSURGO dbase


## Advanced: Starting from Scratch on new coding project

1. setting up venv for specific Python version:
   1. ```
      py -0
      ```

      #lists all Pythons on Windows PC

Need to setup venv (Python 3.9) - previous Python version, as 3.10 does not support Pandas in a full might yet (June 2022). 

`py -m virtualenv -p="C:\Python\py39\python.exe" "C:\c_repos\soils-ssurgo\.venv39"`

2. Activate the environment and install modules
   `.venv39/scripts/activate`

   `pip install pandas`
3. Create .gitignore and add path to venv there (i.e. type there ".venv39")
4. Create requirements.txt for this repo with the enviroment packages installed

`python freeze > requirements.txt`
