#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <list>
#include <algorithm>
using namespace std;

class date{
public:
	char name[6];
	int year;
	int mon;
	int day;
	date(char *name, int year, int mon, int day){
		for (int i = 0; i < 6; i++)
			this->name[i] = name[i];
		this->year = year;
		this->mon = mon;
		this->day = day;
	}
	friend bool operator<(date &d1, date &d2){
		if (d1.year < d2.year)
			return true;
		else if (d1.year == d2.year){
			if (d1.mon < d2.mon)
				return true;
			else if (d1.mon == d2.mon){
				return d1.day < d2.day;
			}
			else
				return false;
		}
		else
			return false;
	}

	friend bool operator>(date &d1, date &d2){
		if (d1.year > d2.year)
			return true;
		else if (d1.year == d2.year){
			if (d1.mon > d2.mon)
				return true;
			else if (d1.mon == d2.mon){
				return d1.day > d2.day;
			}
			else
				return false;
		}
		else
			return false;
	}

	friend bool operator==(date &d1, date &d2){
		return d1.year == d2.year && d1.mon == d2.mon && d1.day == d2.day;
	}
};
int main()
{
	int num, eff_num = 0;
	scanf("%d", &num);
	list<date> datelist;
	date today("", 2014, 9, 6);
	date min("", 1814, 9, 6);
	for (int i = 0; i < num; i++){
		char name[6];
		int year, mon, day;
		scanf("%s %d/%d/%d", name, &year, &mon, &day);
		date cur(name, year, mon, day);
		if (cur < min || cur > today)
			continue;
		eff_num++;
		datelist.push_back(cur);
	}
	if (eff_num){
		printf("%d ", eff_num);
		list<date>::iterator it;
		it = min_element(datelist.begin(), datelist.end());
		printf("%s ", (*it).name);
		it = max_element(datelist.begin(), datelist.end());
		printf("%s", (*it).name);
		
	}
	else{
		printf("%d", eff_num);
	}
	return 0;
}