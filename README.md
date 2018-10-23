**ACI Port Finder**

Simple set of scripts that will print all ports in a given ACI cluster

It includes an apic.py file with examples on how to create and retrieve different objects from ACI

Contacts:
* Cesar Obediente ( cobedien@cisco.com )
* Santiago Flores ( sfloresk@cisco.com )

**Source Installation**

It might make sense for you to create a Python Virtual Environment before installing the requirements file. For information on utilizing
a virtual environment please read http://docs.python-guide.org/en/latest/dev/virtualenvs/. Once you have a virtual environment active then
install the packages in the requirements file.

```
(virtualenv) % pip install -r requirements.txt
```

Once the requirements are installed, make sure to add your APIC credentials on the main.py file

***Note: In production applications, never add credentials directly into the code***

To run the the application execute in the root directory of the distribution:
```
python main.py
```

