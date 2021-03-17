9.4: Restrict Unnecessary or Unauthorized Browser and Email Client Extensions
=========================================================
Restrict, either through uninstalling or disabling, any unauthorized or unnecessary browser or email client plugins, extensions, and add-on applications.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Aurhorized software inventory

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets subject to browser/email plugin restrictions (M1)
#. Use :code:`GV5` to identify authorized browser and email plugins
#. For each asset listed in Operation 1, collect the list of installed browser plugins and compare to the output of Operation 2
	#. Identify and enumerate assets with only authorized browser plugins installed or enabled (M2)
	#. Identify and enumerate assets with one or more unauthorized browser plugins installed or enabled (M3)
#. For each asset listed in Operation 1, collect the list of installed email plugins and compare to the output of Operation 2
	#. Identify and enumerate assets with only authorized email plugins installed or enabled (M4)
	#. Identify and enumerate assets with one or more unauthorized browser plugins installed or enabled (M5)

Measures
--------
* M1 = Count of assets subject to browser/email plugin restrictions
* M2 = Count of assets with only authorized browser plugins installed or enabled
* M3 = Count of assets with unauthorized browser plugins installed or enabled
* M4 = Count of assets with only authorized email plugins installed or enabled
* M5 = Count of assets with unauthorized email plugins installed or enabled


Metrics
-------

Browser Plugin Enforcement Quality
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets compliant with authorized browser plugins.
	* - **Calculation**
	  - :code:`M2 / M1`

Email Client Plugin Enforcement Quality
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets compliant with authorized email plugins.
	* - **Calculation**
	  - :code:`M4 / M1`

.. history
.. authors
.. license
