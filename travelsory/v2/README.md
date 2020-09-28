# travel-advisory v1
# Usage
```
git clone git@github.com:iamsuman/travel-advisory.git
cd travel-advisory/travelsory/v2
pip install -r requirements.txt
Usage: 
python lookup2.py --countryCode=AU
python lookup2.py --countryCode='{"countryCode": ["AU","XYZ"]}'
```

Sample Output
```
python lookup2.py --countryCode=AU
Australia


python lookup2.py --countryCode='{"countryCode": ["AU","XYZ"]}'
{'AU': 'Australia', 'XYZ': '404: Country Code does not exist'}

```