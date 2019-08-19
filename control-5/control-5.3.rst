5.3: Securely Store Master Images
=========================================================
Store the master images and templates on securely configured servers, validated with integrity monitoring tools, to ensure that only authorized changes to the images are possible.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Status
------
Draft

Inputs
------
#. The list of master images/templates
#. An available integrity monitoring tool
#. The inventory of master images mapped to the output of the integrity monitoring tool's identifying information (such as a hash).
#. A documented procedure detailing authorizations required for updates to the master images/templates

Operations
----------
#. Collect the list of master images/templates' integrity monitoring identifying information (i.e. for each master image, collect the hash).
#. Determine whether the update procedure documentation exists (M3)

Measures
--------
* M1 = The number of master images/templates
* M2 = The number of master images/templates identified by integrity monitoring tools
* M3 = 1 if the documented master image update procedure exists; 0 otherwise.

Metrics
-------

Integrity Monitoring Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of master images/templates identified by integrity monitoring tools, 
	    | to the total number of images/templates.
	* - **Calculation**
	  - :code:`M2 / M1`

Update Procedures
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Determine if the documented master image update procedure exists
	* - **Calculation**
	  - :code:`M3 == 1`

.. history
.. authors
.. license