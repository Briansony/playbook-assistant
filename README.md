ansible-knife
=============

Installation:
----------

pip install ansible_knife

Create new playbook:
-------------------

Next command create new playbook. Use 'full' or 'default' mode for playbook creation.

`ansible-knife create --roles common install --task=create --mode=full --name=my_playbook --path=/opt`

or

`ansible-knife create -r common install -t create -m full -n my_playbook -p /opt`

Directories structure depending on mode:
----------------------------------------

full:
___
my_playbook/
&nbsp;&nbsp;&nbsp;&nbsp;group_vars/
&nbsp;&nbsp;&nbsp;&nbsp;host_vars/
&nbsp;&nbsp;&nbsp;&nbsp;roles/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role1/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tasks/ 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;handlers/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;templates/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;files/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vars/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;meta/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;....
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rolen/ # same kind of structure as "role1"
&nbsp;&nbsp;&nbsp;&nbsp;hosts
&nbsp;&nbsp;&nbsp;&nbsp;site.yml
           
default:
___
my_playbook/
&nbsp;&nbsp;&nbsp;&nbsp;roles/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role1/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tasks/ 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;templates/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vars/
&nbsp;&nbsp;&nbsp;&nbsp;....
&nbsp;&nbsp;&nbsp;&nbsp;rolen/ # same kind of structure as "role1"
&nbsp;&nbsp;&nbsp;&nbsp;hosts
&nbsp;&nbsp;&nbsp;&nbsp;site.yml
           
Use -w or --without_inventory flag if you want to deprecate inventory file creation:
---------------

`ansible-knife create -r common install -t create -m default -n my_playbook -p /opt -w`    

or

`ansible-knife create --roles common install --task=create --mode=default --name=my_playbook --path=/opt --without_inventory`


Use add command for add new role to existing playbook:
--------------------

`ansible-knife add --roles install  --task=add --mode=full --name=my_playbook --path=/opt`

or

`ansible-knife add -r install  -t add -m full -n my_playbook -p /opt`


Default mode is default, so it is not required option.


Use download command for download your playbooks from github repo:
------------------

`ansible-knife download --url=https://github.com/my_repo/AnsiblePlaybooks.git --path=/opt`
