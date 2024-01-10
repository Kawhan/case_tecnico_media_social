# case_tecnico_media_social

## 🤖 Run project
1° Create virtual ambient <br/>
Windows use this tutorial: <a href="https://www.codingforentrepreneurs.com/guides/install-python-on-windows/">Tutorial</a> </br>
Ubuntu use this tutorial: <a href="https://www.codingforentrepreneurs.com/guides/install-python-on-windows/](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart)https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart">Tutorial</a> <br/>


2° Run the project<br/>
<ol align="left">
  <li>Activate the virtual environment, this information on how to activate the virtual environment can be accessed through this tutorial: <a href="https://ioflood.com/blog/python-activate-venv/#:~:text=Activating%20a%20virtual%20environment%20in%20Python%20is%20straightforward.,directory%20of%20your%20virtual%20environment.">Tutorial</a></li>
  <li>Install all dependencies using the command: pip install -r requirements.txt</li>
  <li>Stop the django container that is running and leave only the postgres container</li>
  <li>Start the project using the command: python manage.py runserver</li>
</ol>