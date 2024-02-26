# Multi-Shard Script
This script allows you to execute the same commands on multiple MySQL hosts simultaneously.

    Note: While not necessarily the optimal solution, it gets the job done! 😄


# Installation
    pip install -r requirements.txt
# Usage
* Change ``` configs = [
    {'host': 'Host', 'username': 'user', 'password': 'pass', 'database': 'db'}
]```
* Run ```python3 multi-shard.py```
