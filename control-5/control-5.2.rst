5.2: Use Unique Passwords
=========================================================
Use unique passwords for all enterprise assets. Best practice implementation includes, at a minimum, an 8-character password for accounts using MFA and a 14-character password for accounts not using MFA. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
------
#. :code:`GV20`: Unique password policy for the enterprise

Operations
----------
#. Check if the enterprise has a unique password policy
	#. If policy is available M1 = 1
	#. Otherwise M1 = 0
#. Review the policy and determine whether it includes password guidance for accounts without MFA
	#. If guidance is included M2 = 1
		#. Does guidance, at a minimum, require a fourteen character password
			#. If password guidance is fourteen characters or longer M3 = 1
			#. Otherwise M3 = 0
	#. Otherwise M2 = 0
#. Review the policy and determine whether it includes password guidance for accounts with MFA
	#. If guidance is included M4 = 1
		#. Does guidance, at a minimum, require an eight character password
			#. If password guidance is eight characters or longer M5 = 1
			#. Otherwise M5 = 0
	#. Otherwise M3 = 0
 
Measures
--------
* M1 = Does a password policy exist 
* M2 = Does guidance exist for accounts without MFA 
* M3 = Does guidance for accounts without MFA meet minimum guidance 
* M4 = Does guidance exist for accounts with MFA
* M5 = Does guidance for accounts with MFA meet minimum guidance 

Metrics
-------
If M1 is 0, the safeguard recieves a failing score. Other metrics don't apply 

Completeness of Password Policy
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of completeness of the unique password policy
	* - **Calculation**
	  - :code:`(M2 + M4) / 2`

Strength of Policy
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of password guidance that meets minimum character length
	    | standards
	* - **Calculation**
	  - :code:`(M3 + M5) / 2`

.. history
.. authors
.. license
