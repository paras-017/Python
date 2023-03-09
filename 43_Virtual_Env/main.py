# How to create a vitual Env
'''
1--> create a folder
2--> run  python -m venv myenv
3--> activate the environment by running command: source myenv/bin/activate
          (myenv) beluga@linux:~/code/Python/43_Virtual_Env$
3--> import any required module ex: pandas 
4--> pip3 install pandas OR pip3 install pandas==1.4.4     (for older version)

# how to deacticate Virtual ENV 
1-->deactivate


#How to create a another Virtual ENV
1--> run python -m venv parasEnv

'''
import pandas as pd
print(pd.__version__)


# Now suppose thier is so many  module installed in you env
'''  
How to check install modules
run: pip freeze
NOTE:  if you want txt file of install modules names run: pip freeze > requirements.txt
   
NOTE:to install all modules in the requirements.txt on friends system 
run : pip install -r requirements.txt
'''
