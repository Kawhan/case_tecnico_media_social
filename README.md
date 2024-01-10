# case_tecnico_media_social

## 🤖 Run project
1° Create virtual ambient <br/>
Windows use this tutorial: <a href="https://www.codingforentrepreneurs.com/guides/install-python-on-windows/">Tutorial</a> </br>
Ubuntu use this tutorial: <a href="https://www.codingforentrepreneurs.com/guides/install-python-on-windows/](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart)https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart">Tutorial</a> <br/>


2° Run the project<br/>
<ol align="left">
  <li>Activate the virtual environment, this information on how to activate the virtual environment can be accessed through this tutorial: <a href="https://ioflood.com/blog/python-activate-venv/#:~:text=Activating%20a%20virtual%20environment%20in%20Python%20is%20straightforward.,directory%20of%20your%20virtual%20environment.">Tutorial</a></li>
  <li>Install all dependencies using the command: pip install -r requirements.txt</li>
  <li>Use: python manage.py migrate. To appling all migrates<li>
  <li>Start the project using the command: python manage.py runserver</li>
</ol>

3° Run the short linux tutorial project<br/>
<ol align="left">
  <li>Create a virtual enviroment: python -m venv ./venv</li>
  <li>Activate virtual enviroment: source venv/bin/activate</li>
  <li>Install all dependencies using the command: pip install -r requirements.txt</li>
  <li>Use: python manage.py migrate. To appling all migrates<li>
  <li>If you can create a superuser using: python manage.py createsuperuser<li>
  <li>Start the project using the command: python manage.py runserver</li>
</ol>

4° Run the short linux tutorial project using python3<br/>
<ol align="left">
  <li>Create a virtual enviroment: python3 -m venv ./venv</li>
  <li>Activate virtual enviroment: source venv/bin/activate</li>
  <li>Install all dependencies using the command: pip install -r requirements.txt</li>
  <li>Use: python3 manage.py migrate. To appling all migrates<li>
  <li>If you can create a superuser using: python3 manage.py createsuperuser<li>
  <li>Start the project using the command: python3 manage.py runserver</li>
</ol>


5° Swagger docs Url: http://127.0.0.1:8000/swagger/