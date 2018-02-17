## Setting up the environment
```
# Python 3
$ git clone <url>
$ cd <folder>
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install -r packages.txt
```

## Test Run
```
$ python main.py
```

## Sample Output
```
$ python main.py 
WARNING:root:Requests made without an app_token will be subject to strict throttling limits.
{ 'address': '200 Block of DONAHUE ST',
  'category': 'RECOVERED VEHICLE',
  'date': '2007-05-18T00:00:00.000',
  'dayofweek': 'Friday',
  'descript': 'RECOVERED VEHICLE - STOLEN OUTSIDE SF',
  'incidntnum': '070504991',
  'location': { 'coordinates': [-122.370590793832, 37.728408061778],
                'type': 'Point'},
  'pddistrict': 'BAYVIEW',
  'pdid': '7050499107055',
  'resolution': 'NONE',
  'time': '00:48',
  'x': '-122.370590793832',
  'y': '37.7284080617777'}
(myenv) elam3-Air:bad-cookie-v2 edisonlam$ 
```

## Resources
* https://data.sfgov.org/Public-Safety/Police-Department-Incidents/tmnf-yvry
* https://dev.socrata.com/foundry/data.sfgov.org/cuks-n6tp

