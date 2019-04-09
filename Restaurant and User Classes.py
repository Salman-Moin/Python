{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Restaurant name is: Daily Restaurantand its cuisine type is Desi\n",
      "Restaurant name is Daily Restaurant and its cuisine type is Desi\n",
      "Welcome!! Restaurant is open!!\n",
      "Restaurant name is Malik Restaurant and its cuisine type is Desi\n",
      "Restaurant name is China Town and its cuisine type is Chinese\n",
      "Restaurant name is Usmania and its cuisine type is Desi/ Continental\n"
     ]
    }
   ],
   "source": [
    "class Restaurant():\n",
    "    def __init__(self, rest_name, cuisine_type):\n",
    "        self.rest_name = rest_name\n",
    "        self.cuisine_type = cuisine_type\n",
    "    def describe_rest(self):\n",
    "        print(\"Restaurant name is \" + self.rest_name.title() + \" and its cuisine type is \" + self.cuisine_type.title())\n",
    "    def open_rest(self):\n",
    "        print(\"Welcome!! Restaurant is open!!\")\n",
    "restaurant = Restaurant(\"Daily Restaurant\", \"Desi\")\n",
    "print(\"Restaurant name is: \" + restaurant.rest_name.title() + \"and its cuisine type is \" + restaurant.cuisine_type)\n",
    "restaurant.describe_rest()\n",
    "restaurant.open_rest()\n",
    "rest1 = Restaurant(\"malik restaurant\", \"desi\")\n",
    "rest2 = Restaurant(\"china town\", \"chinese\")\n",
    "rest3 = Restaurant(\"usmania\", \"desi/ continental\")\n",
    "rest1.describe_rest()\n",
    "rest2.describe_rest()\n",
    "rest3.describe_rest()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dear Sarfaraz Welcome aboard...we wish you a very happy career in our company\n",
      "user1 Sarfaraz Ahmed Finance manager A+ true\n",
      "Dear Waseem Welcome aboard...we wish you a very happy career in our company\n",
      "user2 Waseem Akram Finance clerk A+ true\n",
      "Dear Imran Welcome aboard...we wish you a very happy career in our company\n",
      "user3 Imran Khan Sales general manager A+ true\n",
      "Dear Waqar Welcome aboard...we wish you a very happy career in our company\n",
      "user4 Waqar Yunus Operations supervisor B true\n",
      "Dear Jahangir Welcome aboard...we wish you a very happy career in our company\n",
      "user5 Jahangir Khan Hr manager A true\n"
     ]
    }
   ],
   "source": [
    "class User():\n",
    "    def __init__(self, login_id, fname, lname, dept, role, security_level):\n",
    "        self.login_id = login_id\n",
    "        self.fname = fname\n",
    "        self.lname = lname\n",
    "        self.dept = dept\n",
    "        self.role = role\n",
    "        self.security_level = security_level\n",
    "        self.user_active = \"true\"\n",
    "    def describe_user(self):\n",
    "        print(self.login_id, self.fname.title(), self.lname.title(), self.dept.title(), self.role, self.security_level, self.user_active)\n",
    "    def greet_user(self):\n",
    "        print(\"Dear \" + self.fname.title() + \" Welcome aboard...we wish you a very happy career in our company\")\n",
    "\n",
    "user1 = User(\"user1\", \"sarfaraz\", \"ahmed\", \"finance\", \"manager\", \"A+\")\n",
    "user2 = User(\"user2\", \"waseem\", \"akram\", \"finance\", \"clerk\", \"A+\")\n",
    "user3 = User(\"user3\", \"imran\", \"khan\", \"sales\", \"general manager\", \"A+\")\n",
    "user4 = User(\"user4\", \"waqar\", \"yunus\", \"operations\", \"supervisor\", \"B\")\n",
    "user5 = User(\"user5\", \"jahangir\", \"khan\", \"hr\", \"manager\", \"A\")\n",
    "user1.greet_user()\n",
    "user1.describe_user()\n",
    "user2.greet_user()\n",
    "user2.describe_user()\n",
    "user3.greet_user()\n",
    "user3.describe_user()\n",
    "user4.greet_user()\n",
    "user4.describe_user()\n",
    "user5.greet_user()\n",
    "user5.describe_user()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
