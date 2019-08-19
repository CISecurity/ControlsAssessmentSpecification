1.7: Deploy Port Level Access Control
=========================================================
Utilize port level access control, following 802.1x standards, to control which devices can authenticate to the network. The authentication system shall be tied into the hardware asset inventory data to ensure only authorized devices can connect to the network.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Status
------
Draft

Assumptions
^^^^^^^^^^^
#. Use of an 802.1x network design to control network access
#. The 802.1x system can query the endpoint inventory system
#. The CMDB is a separate entity from the authentication server.

Inputs
------
#. List of 802.1x authenticators
#. List of 802.1x authentication servers (i.e. RADIUS/Diameter servers)
#. List of CMDB servers

Operations
----------
#. For each 802.1x authenticator, ensure proper configuration
#. For each 802.1x authentication server, ensure proper configuration, including connection to at least one CMDB server

Measures
--------
* M1 = Boolean: 802.1x authenticators are in use
* M2 = Boolean: 802.1x authentication servers are in use
* M3 = Count of improperly configured 802.1x authenticators
* M4 = Count of 802.1x authenticators
* M5 = Count of improperly configured 802.1x authentication servers
* M6 = Count of 802.1x authentication servers

Metrics
-------

802.1x Deployment
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Is 802.1x deployed?
	* - **Calculation**
	  - :code:`M1 AND M2`

Authenticator Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of improperly configured 802.1x authenticators to total number of 802.1x 
	    | authenticators
	* - **Calculation**
	  - :code:`M3 / M4`

Authentication Server Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of improperly configured 802.1x authentication servers to total number of 
	    | 802.1x authentication servers
	* - **Calculation**
	  - :code:`M5 / M6`

.. history
.. authors
.. license