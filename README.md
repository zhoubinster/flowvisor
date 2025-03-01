# Installation of Flowvisor on Ubuntu 20.04/24.04

## Preparation
Please download the SEED Ubuntu 20.04 VM from [SEED Labs](https://seedsecuritylabs.org/labsetup.html) which we use in courses 620,615,745. This guide has been tested in this environment, but it should also work on versions above Ubuntu 20.04.

--- 

## Installation Steps
### Step 1: Install Prerequisites
Install necessary tools. If already installed, skip this step.
```bash
sudo apt install gcc make git tar -y
```
### Step 2: Install Mininet
```bash
sudo apt install mininet -y
```
### Step 3: Install JDK
```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
```
### Step 4: Install Apache Ant
```bash
sudo apt install ant -y
```
### Step 5: Install python-is-python3
This allows the use of python instead of python3.
```bash
sudo apt install python-is-python3 -y
```
### Step 6: Download the Flowvisor Code
**Important**: Do not use the official version, as this guide references a modified version. You may fork this branch to create your own version.
```bash
git clone https://github.com/zhoubinster/flowvisor.git
```
### Step 7: Install Flowvisor
```bash
cd flowvisor/
make
sudo make install
```
### Step 8: Configure Flowvisor
Set permissions and load the configuration. Please replace 'seed:seed' with your own 'username:usergroup.':
```bash
sudo chown seed:seed -R /usr/local/share/db
sudo chmod -R 777 /usr/local/share/db
fvconfig load /etc/flowvisor/config.json
```
### Step 9: Test Flowvisor
1. Create the password file using the vi command.
2. Set the configuration:
```bash
fvctl -f pwd set-config --enable-topo-ctrl
```
## Additional Tips and Notes
### 1. OpenFlow Protocol Support
FlowVisor supports OpenFlow 1.0 only. When creating the topology, include the following parameter to specify the protocol:
```bash
--switch ovsk,protocols=OpenFlow10
```
For example:
```bash
sudo mn --custom custom-fat-tree-8pods.py --topo fattree --link=tc --arp --mac --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow10
```
### 2. Java Remote Debug Port
The default Java remote debug port is 5005. Use this port for debugging the program.
### 3. POX Controller
- **Requirement:** POX requires Python 3. Ensure it is installed.
- **Installation:**
```bash
git clone https://github.com/noxrepo/pox.git
```
- **Run POX Controller:**
```bash
sudo ./pox.py forwarding.l2_learning openflow.of_01 --address=127.0.0.1 --port=4000
```
### 4. FlowVisor Runtime Logs
To monitor FlowVisor logs, use the following command:
```bash
tail -f /var/log/flowvisor/test.log
```
### 5. Remove ^M Characters
If files transferred from Windows to Ubuntu contain ^M characters, use this command to remove them:
```bash
sed -i 's/\r//' filename
```
### 6. Some commands used in flowvisor
Create slice:
```bash
fvctl -f pwd add-slice Purple tcp:127.0.0.1:4000 admin@Purple
```
List all slices:
```bash
fvctl -f pwd list-slices
```
View slice info:
```bash
fvctl -f pwd list-slice-info Purple
```
Remove slice:
```bash
fvctl -f pwd remove-slice Purple
```
Add a flowspace rule:
```bash
fvctl -f pwd add-flowspace purple_acc_s4_1 0300000000000004 1 in_port=2 Purple=7
```
Remove a flowspace rule:
```bash
fvctl -f pwd remove-flowspace purple_acc_s4_1
```
List all flowspace rules:
```bash
fvctl -f pwd list-flowspace
```

About FlowVisor
=========
    An OpenFlow controller that acts as a hypervisor/proxy
    between a switch and multiple controllers.  Can slice
    multiple switches in parallel, effectively slicing a network.

Documentation
=============

    Start with the INSTALL file and then refer to:
        https://www.flowvisor.org
    Also, the manpages are in the ./doc directory and can be viewed
    without installing them using `man ./doc/fvctl.1`

    For developers, check out README.dev and the architecture diagrams:
        https://github.com/OPENNETWORKINGLAB/flowvisor/wiki under the developement section
    Also, `make docs` produces the source code documentation and
    there are manpages under ./doc

Questions
=========

    openflow-discuss@openflowswitch.org