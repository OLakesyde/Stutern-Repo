#!/usr/bin/env python
# coding: utf-8

# In[1]:




last_name		first_name	Position			Salary		Hired	

Lew
Sessom
HENDERSON
Lanier			Cathy		Chief				230743		1990
Arons			Bernard		Medical Officer Psych		206000		2008
Ritchie			Elspeth		Medical Officer Psych		206000		2010
GRAY			VINCENT		Mayor				200000		2005
Marshall		Katherine	Medical Officer Psych		200000		2008
Gandhi			Natwar		Chief Financial Officer		199700		1997
DUNCAN			LORETTA		Workers Compensation Recipient	197808		1984
Baxter			Graeme		Act Provost & Vp Acd Aff	196257		2008
Miramontes		David		Medical Director		193125		2011
Graves			Warren		Chief Of Staff			193125		2011
Stanchfield		Eric		Executive Director		193125		2007
Jones			Tyler		Medical Officer Psych		190550		2008
BROWN			KWAME		Chairman			190000		2005
Eure			Philip		Executive Director		188692		2000
Cooper			Ginnie		Executive Director		188044		2006
Yadao			Nilda		Medical Officer (psychiatry)	188027		1987
Ellerbe			Kenneth		Fire Chief			187302		2003
Ruland			Jeffrey		Dir Of The Ctr For Wf Str & Ec	186911		2009
Parker			Craig		General Counsel			186911		2009
Farley			Mark		Vp, Human Resources		186911		2008
Otero			Beatriz		Dep Mayor For Hlth & Hum Svcs	185000		2011
Quander			Paul		Deputy Mayor			185000		2009
Pierre 			Louis		Marie	Chief Medical Examiner	185000		1985
Pestaner		Joseph		Medical Officer (medical Exami	183892		1997
Revercomb		Carolyn		Medical Officer (medical Exami	183892		2005
Morgan 			Johnson		Sheila	Chief Investment Officer183677		1991
Williamson		Michael		Deputy Director			182000		2011
White			Mattie		Medical Officer (psychiatry)	180604		1989
Park			Kyung		Medical Officer (psychiatry)	180604		1987
Gore			T		Medical Officer (psychiatry)	172101		2005
LUDWIG			BENJAMIN	Workers Compensation Recipient	171517		1972
Atdjian			Sylvia		Medical Officer (psychiatry)	170938		2007
Zaidi			Syed		Medical Officer (psychiatry)	170344		2005
Sherron			Robert		Medical Officer (psychiatry)	170344		1991
Johnson			Nicole		Medical Officer (psychiatry)	170344		2007
RUDA			LISA		Chief Of Staff			170000		2007
Beers			Nathaniel	Deputy Superintendent		170000		2007
Nuss			Laura		Director			170000		2007
Mancini			Robert		Acting Director			170000		2004
Wicker			Henry		Medical Officer Opthal		168378		1987
Davenport		Nancy		Administrative Librarian	167200		2006
Jaji			Abayomi		Medical Officer (psychiatry)	167062		2000
Stevens			KyleeAnn	Medical Officer (psychiatry)	167051		2008
Smothers		Kenneth		Medical Officer (psychiatry)	166995		1987
Akhtar			Saleha		Medical Officer (psychiatry)	166995		1988
Singh			Anjali		Medical Officer (psychiatry)	166370		1999
Rahman			Umar		Medical Officer (psychiatry)	166370		1996
Adewale			Benjamin	Medical Officer (psychiatry)	166370		1988
Zaidi			Syed		Medical Officer General Practi	165842		1983
Jackson			Kenneth		Assistant Fire Chief Srvs	165306		1982
Berns			David		Dir Of Human Services		165200		2011
Cordi			Stephen		Deputy Cfo Otr			165162		2008
Mallory			Lisa		Acting Director			165000		2004
Flowers			Brian		General Counsel			165000		1985
Bellamy			Terry		Director			165000		2008
West			Millicent	Director, Homeland Sec & Ema	165000		2003
Pappas			Gregory		Deputy Dir			164800		2011
Altaf			Samia		Supervisor Medical Officer	164800		2010
Owens


# In[2]:


pip install ipython-sql


# In[3]:


pip install ipython-sql


# In[4]:


get_ipython().run_line_magic('reload_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///university.db')


# In[5]:


get_ipython().run_cell_magic('sql', '', 'CREATE TABLE employees (employee_id integer PRIMARY KEY AUTOINCREMENT,\n                        last_name text,\n                        first_name text,\n                        Position text,\n                        Salary integer,\n                        date_hired integer\n                       );')


# In[7]:


get_ipython().run_cell_magic('sql', '', "INSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Lew', 'Allen', 'City Administrator', 295000, 2004);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Sessoms', 'Allen', 'President', 295000, 2008 );\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('HENDERSON', 'KAYATANYA', 'Superintendent Of Schools', 275000, 2007 );\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Lanier', 'Cathy', 'Chief', 230743, 1990 );\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Arons', 'Bernard', 'Medical Officer Psych', 206000, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Ritchie', 'Elspeth', 'Medical Officer Psych', 206000, 2010);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('GRAY','VINCENT', 'Mayor', 200000, 2005 );\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Marshall', 'Katherine', 'Medical Officer Psych', 200000, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Gandhi', 'Natwar', 'Chief Financial Officer', 199700, 1997 );\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('DUNCAN', 'LORETTA', 'Workers Compensation Recipient', 197808, 1984);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Baxter', 'Graeme', 'Act Provost & Vp Acd Aff', 196257, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Miramontes', 'David', 'Medical Director', 193125, 2011);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Graves', 'Warren','Chief Of Staff', 193125, 2011);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Stanchfield', 'Eric', 'Executive Director', 193125, 2007);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Jones', 'Tyler', 'Medical Officer Psych', 190550, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('BROWN', 'KWAME', 'Chairman', 190000, 2005);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Eure', 'Philip', 'Executive Director', 188692, 2000);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Cooper', 'Ginnie', 'Executive Director', 188044, 2006);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Yadao', 'Nilda', 'Medical Officer (psychiatry)', 188027, 1987);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Ellerbe', 'Kenneth', 'Fire Chief', 187302, 2003);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Ruland', 'Jeffrey', 'Dir Of The Ctr For Wf Str & Ec', 186911, 2009);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Parker', 'Craig', 'General Counsel', 186911, 2009);\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Farley', 'Mark', 'Vp, Human Resources', 186911, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Otero', 'Beatriz', 'Dep Mayor For Hlth & Hum Svcs', 185000, 2011);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Quander', 'Paul', 'Deputy Mayor', 185000, 2009);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Pierre', 'Louis', 'Marie Chief Medical Examiner', 185000, 1985);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Pestaner', 'Joseph', 'Medical Officer (medical Exami)', 183892, 1997);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Revercomb', 'Carolyn', 'Medical Officer (medical Exami)', 183892, 2005);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Morgan', 'Johnson', 'Sheila Chief Investment Officer', 183677, 1991);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Williamson', 'Michael', 'Deputy Director', 182000, 2011);\n                                            \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('White', 'Mattie', 'Medical Officer (psychiatry)', 18060, 1989);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Park', 'Kyung', 'Medical Officer (psychiatry)', 180604, 1987);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Gore', 'T', 'Medical Officer (psychiatry)', 172101, 2005);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('LUDWIG', 'BENJAMIN', 'Workers Compensation Recipient', 171517, 1972);\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Atdjian', 'Sylvia', 'Medical Officer (psychiatry)', 170938, 2007);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Zaidi', 'Syed', 'Medical Officer (psychiatry)', 170344, 2005);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Sherron', 'Robert', 'Medical Officer (psychiatry)', 170344, 1991);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Johnson', 'Nicole',' Medical Officer (psychiatry)', 170344, 2007);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('RUDA', 'LISA', 'Chief Of Staff', 170000, 2007);\n                                             \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Beers', 'Nathaniel', 'Deputy Superintendent', 170000, 2007);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Nuss', 'Laura', 'Director', 170000, 2007);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Mancini', 'Robert', 'Acting Director', 170000, 2004);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Wicker', 'Henry', 'Medical Officer Opthal', 168378, 1987);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Davenport', 'Nancy', 'Administrative Librarian', 167200, 2006);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Jaji', 'Abayomi', 'Medical Officer (psychiatry)', 167062, 2000);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Stevens', 'KyleeAnn', 'Medical Officer (psychiatry)', 167051, 2008);\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Smothers', 'Kenneth', 'Medical Officer (psychiatry)', 166995, 1987);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Akhtar', 'Saleha', 'Medical Officer (psychiatry)', 166995, 1988);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Singh', 'Anjali', 'Medical Officer (psychiatry)', 166370, 1999);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Rahman', 'Umar', 'Medical Officer (psychiatry)', 166370, 1996);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Adewale', 'Benjamin', 'Medical Officer (psychiatry)', 166370, 1988);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Zaidi', 'Syed', 'Medical Officer General Practi', 165842, 1983);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Jackson', 'Kenneth', 'Assistant Fire Chief Srvs', 165306, 1982);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Berns', 'David', 'Dir Of Human Services', 165200, 2011);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Cordi', 'Stephen', 'Deputy Cfo Otr', 165162, 2008);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Mallory', 'Lisa', 'Acting Director', 165000, 2004);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Flowers', 'Brian', 'General Counsel', 165000, 1985);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Bellamy', 'Terry', 'Director', 165000, 2008);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('West', 'Millicent', 'Director, Homeland Sec & Ema', 165000, 2003);\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Pappas', 'Gregory', 'Deputy Dir', 164800, 2011);\n        \nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Altaf', 'Samia', 'Supervisor Medical Officer', 164800, 2010);\n\nINSERT INTO employees(last_name, first_name, Position, Salary, date_hired)\nVALUES ('Owens', 'Karen', 'Dental Officer', 164800, 1989);")


# In[8]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM sqlite_master')


# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM employees')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT(Position)\nFROM employees')


# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM employees\nORDER BY first_name DESC\nLIMIT 5')


# In[12]:


get_ipython().run_cell_magic('sql', '', 'SELECT first_name, last_name, salary\nFROM employees\nWHERE salary > 200000')


# In[13]:


get_ipython().run_cell_magic('sql', '', "SELECT *\nFROM employees\nWHERE last_name LIKE 'R_da'")


# In[14]:


get_ipython().run_cell_magic('sql', '', "UPDATE employees\nSET last_name = 'PETER'\nWHERE first_name = 'LISA'")


# In[15]:


get_ipython().run_cell_magic('sql', '', "SELECT *\nFROM employees\nWHERE first_name LIKE 'LISA'")


# In[16]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM employees\nWHERE employee_id IS 39')


# In[17]:


get_ipython().run_cell_magic('sql', '', "SELECT * \nFROM employees\nWHERE last_name LIKE 'K___E' OR first_name LIKE 'K___E'")


# In[18]:


get_ipython().run_cell_magic('sql', '', 'DELETE \nFROM employees\nWHERE employee_id = 16')


# In[19]:


get_ipython().run_cell_magic('sql', '', 'SELECT * \nFROM employees')


# In[20]:


get_ipython().run_cell_magic('sql', '', "SELECT Position AS 'job_role'\nFROM employees\nLIMIT 5")


# In[21]:


get_ipython().run_cell_magic('sql', '', "SELECT employee_id, first_name AS 'Name', last_name AS 'Name', salary \nFROM employees\nORDER BY salary ASC\nLIMIT 5")


# In[22]:


get_ipython().run_cell_magic('sql', '', 'SELECT COUNT (*)\nFROM employees\nWHERE salary > 200000')


# In[23]:


get_ipython().run_cell_magic('sql', '', 'SELECT MAX(salary), MIN(salary)\nFROM employees')


# In[ ]:




