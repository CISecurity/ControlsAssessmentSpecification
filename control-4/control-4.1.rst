4.1: Maintain Inventory of Administrative Accounts
=========================================================
Use automated tools to inventory all administrative accounts, including domain and local accounts, to ensure that only authorized individuals have elevated privileges.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Detect
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. Inventory of authorized administrative accounts including which system the account is authorized for and which individual the account is associated with
#. Output from the automated tool(s) identifying the discovered administrative accounts accompanied by which system that account is on

Operations
----------
#. Generate a count of the administrative accounts in Inventory 1 (this count becomes M1). If this count is 0, skip the remaining Operation(s).
#. Check Input 2 - if there is at least 1 administrative account provided in Input 2, set M2 equal to 1 and continue on to the next Operation. If there are no administrative accounts provided in Input 2, set M2 equal to 0 and skip the remaining Operation(s).
#. Compare Input 1 and Input 2, creating a list accounts that are in Input 2 which are also found in Input 1 (this is the list of discovered authorized administrative accounts that becomes M3) and a list of accounts that are in Input 2 that are not found in Input 1 (this is the list of discovered unauthorized administrative accounts that becomes M4).

Measures
--------
* M1 = Count of authorized administrative accounts in Input 1
* M2 = A binary value, 1 if the automated tool(s) provided at least 1 administrative account (Input 2); 0 if the automated tool(s) did not provide any administrative accounts (Input 2)
* M3 = List of discovered authorized administrative accounts
* M4 = List of discovered unauthorized administrative accounts
* M5 = Count of discovered authorized administrative accounts
* M6 = Count of discovered unauthorized administrative accounts

Metrics
-------

Administrative Account Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure the administrative account inventory exists.  If :code:`M1 == 0`, this metric
	    | fails and the remaining metrics are not applicable.
	* - **Calculation**
	  - :code:`M1`

Automated Tool Functioning
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure any automated tools are properly functioning.  If :code:`M2 == 0`, this metric
	    | fails and the remaining metrics are not applicable.
	* - **Calculation**
	  - :code:`M2`

Tool Coverage
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio discovered administrative accounts to the inventoried administrative accounts.
	* - **Calculation**
	  - :code:`M5 / M1`

Unauthorized Accounts
^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of discovered unauthorized administrative accounts to total discovered
	    | administrative accounts
	* - **Calculation**
	  - :code:`M6 / (M5 + M6)`

.. history
.. authors
.. license
