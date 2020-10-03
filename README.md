# Key-Logger
A simple program that helps you log your keystrokes.  

Key-Logger doesn't require *administrator* access to log keys. Also it has no dependencies on external libraries, unlike other programs that require *administrator access* even to install them.


###### Note: Currently supports only Linux

### Requirements

No special requirements except **Python3**. 

### Usage
**Add key-logger as executable**

    chmod +x key-logger.sh

**Start logging**

    ./key-logger.sh

Select the **keyboard ID** from the list shown, which you want to log.

**Parse key-log**

    python3 parser.py <log_file>