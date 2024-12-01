# Installation of Flowvisor on Ubuntu 20.04

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
Set permissions and load the configuration:
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

