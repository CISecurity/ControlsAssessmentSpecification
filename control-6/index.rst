CIS Control 6: Access Control Management
=================================================================

Use processes and tools to create, assign, manage, and revoke access credentials and privileges for user, administrator, and service accounts for enterprise assets and software.

**Why is this CIS Control Critical?**

Where CIS Control 5 deals specifically with account management, CIS Control 6 focuses on managing what access these accounts have, ensuring users only have access to the data or enterprise assets appropriate for their role, and ensuring that there is strong authentication for critical or sensitive enterprise data or functions. Accounts should only have the minimal authorization needed for the role. Developing consistent access rights for each role and assigning roles to users is a best practice. Developing a program for complete provision and de-provisioning access is also important. Centralizing this function is ideal. 

There are some user activities that pose greater risk to an enterprise, either because they are accessed from untrusted networks, or performing administrator functions that allow the ability to add, change, or remove other accounts, or make configuration changes to operating systems or applications to make them less secure. This also enforces the importance of using MFA and Privileged Access Management (PAM) tools.

Some users have access to enterprise assets or data they do not need for their role; this might be due to an immature process that gives all users all access, or lingering access as users change roles within the enterprise over time. Local administrator privileges to users’ laptops is also an issue, as any malicious code installed or downloaded by the user can have greater impact on the enterprise asset running as administrator. User, administrator, and service account access should be based on enterprise role and need.


.. toctree::
   :maxdepth: 1
   :name: toc-control-6

   6.1: Establish an Access Granting Process <control-6.1>
   6.2: Establish an Access Revoking Process <control-6.2>
   6.3: Require MFA for Externally-Exposed Applications <control-6.3>
   6.4: Require MFA for Remote Network Access <control-6.4>
   6.5: Require MFA for Administrative Access <control-6.5>
   6.6: Establish and Maintain an Inventory of Authentication and Authorization Systems <control-6.6>
   6.7: Centralize Access Control <control-6.7>
   6.8: Define and Maintain Role-Based Access Control <control-6.8>
   
.. history
.. authors
.. license
