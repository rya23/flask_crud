


echo "BUILD START"
# create a virtual environment named 'venv' if it doesn't already exist
python3.12 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver