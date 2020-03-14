<p align="center">
  <!-- <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a> -->
 <pre style="white-space:pre">
       ,--------------------------.                                         
      ( Change Your WiFi Password! )  .-.
       `--------------------------'    \ \
            (_)                         \ \
                O                       | |
                  o                     | |    ██████╗        █████╗        ████████╗
                    . /\---/\   _,---._ | |   ██╔════╝       ██╔══██╗       ╚══██╔══╝
                     /^   ^  \,'       '. ;   ██║            ███████║          ██║
                    ( O   O   )           ;   ██║            ██╔══██║          ██║
                     `.=o=__,'            \   ╚██████╗██╗    ██║  ██║██╗       ██║██╗
                        /         _,--.__   \  ╚═════╝╚═╝    ╚═╝  ╚═╝╚═╝       ╚═╝╚═╝
                       /  _ )   ,'   `-. `-. \     Charter(networks) Auditing Tool
                      / ,' /  ,'        \ \ \ \             by Edward Ayala
                     / /  / ,'          (,_)(,_)
                    (,;  (,,)
 </pre>
</p>
<span style="font-family:monospace">
<h2 align="center">C.A.T. - Charter<span style="font-size:12px">(networks)</span> Auditing Tool</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Implementing the Aircrack-ng Suite, Wash, and Python3, this tool automates the WiFi auditing process. The tool is catered to target Charter Spectrum networks' default password structure.
<br> 
</p>

## 🧐 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
The WiFi network at your house connects you to the internet, you just type in the password that's on the back of the router and you're connected to the network. That's simple and easy! Although there is a significant danger to this easy process. This password on the back of your router is purposely made simple and easy to remember to cater to the customers(you) but that also makes it simple and easy for malicious hackers to break into your network and wreak havoc. This project demonstrates this vulnerability specifically on Charter Spectrum networks, which universally implements a simple password structure that makes it easy to communicate and remember the password. Using an automated tool, hackers can break into a Charter Spectrum network in minutes and gain access to your sensative private information.

## 🏁 Getting Started <a name = "getting_started"></a>



### Prerequisites <a name = "pre"></a>
<table style="text-align:center">
<thead>
  <tr>
    <td>Operating System</td>
    <td>Working</td>
    <td>Planned</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td><img src="https://img.icons8.com/color/48/000000/linux.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/checked-2--v1.png"/></td>
    <td>-</td>
  </tr>
  <tr>
    <td><img src="https://img.icons8.com/color/48/000000/android-os.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/multiply.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/checked-2--v1.png"/></td>

  </tr>
  <tr>
    <td><img src="https://img.icons8.com/ios-filled/40/000000/mac-os.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/multiply.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/checked-2--v1.png"/></td>
  </tr>
  <tr>
    <td><img src="https://img.icons8.com/officel/40/000000/windows-10.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/multiply.png"/></td>
    <td><img src="https://img.icons8.com/officel/40/000000/checked-2--v1.png"/></td>
  </tr>
</tbody>
</table>

* Aircrack-ng
  * Airmon-ng: Toggle interface mode
  * Airodump-ng: Gather information
  * Aireplay-ng: Send deauth packets
* Wash: Gather information
* Pyrit: Validate handshakes

Installing Aircrack-ng:
```
sudo apt-get install aircrack-ng
```
Installing Wash:
```
sudo apt-get install reaver-wps
```
Installing Pyrit:
```
sudo apt-get install pyrit
```

### Installing

Clone or download via GitHub:
```
git clone https://github.com/edwardayala/CAT.git
```

[Ensure all dependecies are correctly installed](#pre)


## 🎈 Usage <a name="usage"></a>

#### !!!MUST RUN AS ROOT!!!
```
sudo python3 cat.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python3](https://www.python.org/) - Main programming language
- [Linux](https://www.linux.org/) - Using unix terminal
- [Aircrack-ng](https://www.aircrack-ng.org/) - Network auditing tool
- [Wash](https://github.com/t6x/reaver-wps-fork-t6x) - Network auditing tool

## ✍️ Authors <a name = "authors"></a>

- [@edwardayala](https://github.com/edwardayala)
</span>
