<div style="font-family: 'Times New Roman', Times, serif; font-size: 110%">
<div>
<div>
<h2>Requirements <hr>
</h2>
<ul>
<li>Python (3.6, 3.7, 3.8, 3.9, 3.10)</li>
<li>Django (2.2, 3.0, 3.1, 3.2, 4.0)</li>
<li>PostgreSQL (10.21, 11.16, 12.11, 13.7, 14.3)</li>
</ul>

<p>We highly recommend and only officially support the latest patch release of each Python and Django series.</p>
</div>
<div>
<h2>Installation <hr>
</h2>

<p>Install using <code>pip</code>...</p>

<pre>pip install djangorestframework django psycopg2-binary</pre>
</div>
<div>
<h2>Setting <hr>
</h2>
<p>You need open<code>project/.env.dev</code> and connect your database. <br>
<b>Example:</b>
</p>
<pre>
DB_HOST=db         
DB_NAME=p_db       # name database
DB_USER=user       # your user
DB_PASS=password    # your password 
POSTGRES_DB=p_db     # name database
POSTGRES_USER=user    # your user
POSTGRES_PASSWORD=password  # your password 
</pre>
<p>Also you need to download a Docker 
<a href="https://www.docker.com">https://www.docker.com</a>.
How to set up Docker will be written in Docker app.
</p>
</div>
<div>
<h2>Create Docker container and project launch<hr>
</h2>
<p>Go to cmd.exe or bash/zsh and write path to the project. <br>
<b>Example: </b><code>cd /mnt/c/all/project</code>. <br>
Then connect venv <code>$ source venv/bin/activate</code> Linux or Windows <code>venv\Scripts\activate.bat</code> and create container <code>docker-compose up --build</code>. <br>
Now you can run the project in Docker.
</p>

</div>
</div>
</div>