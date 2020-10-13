
# Competitive Calendar


Get a list of all competitive programming contests happening on various sites.

### Supported Sites
- [AtCoder](https://atcoder.jp/)
- [CodeChef](https://codechef.com/)
- [CodeForces](https://codeforces.com/)
- [CodeForces::Gym](https://codeforces.com/gyms)
- [CS Academy](https://csacademy.com/)
- [HackerEarth](https://hackerearth.com/)
- [HackerRank](https://hackerrank.com/)
- [Kick Start](https://codingcompetitions.withgoogle.com/kickstart)
- [LeetCode](https://leetcode.com/)
- [TopCoder](https://topcoder.com/)

## Setup and activate virtual environment

For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```
For Windows users, please execute the following command to create and activate venv.
```
virtualenv venv
"venv/Scripts/activate"
```    
Navigate back to the main folder and install the requirements.
```
pip install -r requirements.txt
```
## How to use

```bash
$ python main.py [-h]  [--today]
```
If not adding any argument, the script will print all the ongoing and future contests by default.
```
optional arguments:

-h, --help show this help message and exit
--today Print only today's contests
```

## Sample Output
```
$ python main.py

Today (13 Oct '20):

        #DeveloperIPL Game [HackerEarth]
        06:00 PM, 09 Oct '20  -  06:00 PM, 25 Oct '20
        Contest URL: https://www.hackerearth.com/challenges/hackathon/developeripl-game/
        
        ProjectEuler+ [HackerRank]
        09:08 PM, 07 Jul '14  -  12:00 AM, 31 Jul '24
        Contest URL: https://hackerrank.com/contests/projecteuler

        DSA Learning Series [CodeChef]
        12:00 AM, 30 Mar '20  -  12:00 AM, 30 Mar '21
        Contest URL: https://www.codechef.com/LEARNDSA?itm_campaign=contest_listing


15 October, 2020:

        Hackccelerate 2020 [HackerEarth]
        11:55 PM, 15 Oct '20  -  11:55 PM, 18 Oct '20
        Contest URL: https://www.hackerearth.com/challenges/hackathon/hackccelerate-2020/


17 October, 2020:

        Code Divas Diversity Challenge 2020 [HackerEarth]
        04:00 PM, 17 Oct '20  -  10:00 PM, 17 Oct '20
        Contest URL: https://www.hackerearth.com/challenges/hiring/code-divas-2020/

        Codeforces Round (Div. 1 + Div. 2) [CodeForces]
        06:35 PM, 17 Oct '20  -  09:05 PM, 17 Oct '20
        Contest URL: https://codeforces.com/contestRegistration/1428

		...
		...
		...
```

### Credits
Thanks to [Kontests](https://github.com/AliOsm/kontests) for their free API which fetches competitive contests details from the above listed sites.

### Contact
Feel sure to contact [Sakshi Uppoor](https://github.com/SakshiUppoor) regarding any suggestions/bugs.