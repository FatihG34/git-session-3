{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "60289343",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):\n",
    "    print(\"-- This parrot wouldn't\", action, end=' ')\n",
    "    print(\"if you put\", voltage, \"volts through it.\")\n",
    "    print(\"-- Lovely plumage, the\", type)\n",
    "    print(\"-- It's\", state, \"!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f2793f45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-- This parrot wouldn't voom if you put 1000 volts through it.\n",
      "-- Lovely plumage, the Norwegian Blue\n",
      "-- It's a stiff !\n"
     ]
    }
   ],
   "source": [
    "parrot(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5491b5d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-- This parrot wouldn't Vooom if you put 100000 volts through it.\n",
      "-- Lovely plumage, the Norwegian Blue\n",
      "-- It's a stiff !\n"
     ]
    }
   ],
   "source": [
    "parrot(voltage=100000, action=\"Vooom\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4fe6136",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fokkk(x, y):\n",
    "    print(x, y, \"yaşındadır\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8b6441ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ali 55 yaşındadır\n"
     ]
    }
   ],
   "source": [
    "fokkk(\"ali\", 55)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "14de1498",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "fokkk() got an unexpected keyword argument 'z'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [10]\u001b[0m, in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mfokkk\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m66\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mz\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmehmet\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mTypeError\u001b[0m: fokkk() got an unexpected keyword argument 'z'"
     ]
    }
   ],
   "source": [
    "fokkk(66, z=\"mehmet\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5414dfe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want to get orange and banana\n"
     ]
    }
   ],
   "source": [
    "def fruiterer(fruit1, fruit2) :\n",
    "    print('I want to get', fruit1, 'and', fruit2)\n",
    "        \n",
    "fruiterer('orange', 'banana')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "be2ce950",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'tuple'>\n"
     ]
    }
   ],
   "source": [
    "def fruiterer(*fruit) :\n",
    "    print(type(fruit))\n",
    "fruiterer('orange', 'banana', 'melon', 'ananas')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f83abb8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want to get :\n",
      "- orange\n",
      "- banana\n",
      "- melon\n",
      "- ananas\n"
     ]
    }
   ],
   "source": [
    "def fruiterer(*fruit) :\n",
    "    print('I want to get :')\n",
    "    for i in fruit :\n",
    "        print('-', i)\n",
    "        \n",
    "fruiterer('orange', 'banana', 'melon', 'ananas')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "affc4ffc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want to get :\n",
      "- melon\n"
     ]
    }
   ],
   "source": [
    "fruiterer(\"melon\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0188920",
   "metadata": {},
   "source": [
    "``` Fonksiyonu çağırırken fonksiyona birden çok argüman yollayabiliyoruz.\n",
    "Bunu yapabilmek için fonksiyonda parametrenin başına * koyuyoruz.\n",
    "Önüne * koyduğumuzda o  parametre iterable hale gelmiş oluyor. Bu nedenle birden fazla değer alabiliyor.\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6db5929a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def slicer(* m):\n",
    "    list_even = []\n",
    "    \n",
    "    list_odd = []\n",
    "    \n",
    "    for i in m:\n",
    "        \n",
    "        if i % 2 == 0:\n",
    "            list_even.append(i)\n",
    "            \n",
    "        else:\n",
    "            list_odd.append(i)\n",
    "    print(\"Evens :\", list_even)\n",
    "    print(\"Odds :\", list_odd)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ee7ea224",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Evens : [2, 4, 6, 8]\n",
      "Odds : [1, 3, 5, 7, 9]\n"
     ]
    }
   ],
   "source": [
    "slicer(1,2,3,4,5,6,7,8,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "eaabf359",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lions are Carnivores\n",
      "Bears are Omnivores\n",
      "Deers are Herbivores\n",
      "Human are Nomnivores\n"
     ]
    }
   ],
   "source": [
    "def animals(**kwargsss):\n",
    "    for key, value in kwargsss.items():\n",
    "        print(value, \"are\", key)\n",
    " \n",
    "animals(Carnivores=\"Lions\", Omnivores=\"Bears\", Herbivores=\"Deers\", Nomnivores=\"Human\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "61235f8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def organizer(**kwrd):\n",
    "    nms = []\n",
    "    age = []\n",
    "    for vvas, vas in kwrd.items():\n",
    "        nms.append(vvas)\n",
    "        age.append(vas)\n",
    "    print(nms)\n",
    "    print(age)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "11c4384c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['beth', 'ali', 'veli', 'deli']\n",
      "[26, 25, 45, 35]\n"
     ]
    }
   ],
   "source": [
    "organizer(beth=26, ali=25, veli= 45, deli=35)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ca237d73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ahmet bacanak\n",
      "mehmet ağabey\n",
      "ceyda baldız\n"
     ]
    }
   ],
   "source": [
    "def sözlük(**a) :  \n",
    "    for key, value in a.items():\n",
    "        print(key, value)\n",
    "    \n",
    "sözlük(ahmet=\"bacanak\", mehmet=\"ağabey\", ceyda=\"baldız\")\n",
    "#  Fonksiyondaa ** koyduğum için bu artık bir sözlüğe dönüştü.\n",
    "#  o yüzden artık fonsiyonu çağırırken keyword argümanlarla çağıracağız.\n",
    "#  ** dan dolayı bu fonksiyona istediğim kadar keyword argüman kullanabiliriz."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f02625d4",
   "metadata": {},
   "source": [
    "### Fibonacci Numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "4a4fb60e",
   "metadata": {},
   "outputs": [],
   "source": [
    "fibo = [1, 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "035009d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(8):\n",
    "    fibo.append(fibo[i] + fibo[i+1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "85d45ace",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fibo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1a61245c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of sequence of Fibonacci. 8\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = int(input(\"Enter the number of sequence of Fibonacci. \"))\n",
    "fibo = [1, 1]\n",
    "for i in range(8):\n",
    "    fibo.append(fibo[i] + fibo[i+1])\n",
    "fibo"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32ead2b0",
   "metadata": {},
   "source": [
    "### bu kadar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b42170d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "filter()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd806058",
   "metadata": {},
   "outputs": [],
   "source": [
    "cümle = \"hadi yapacaksın olacak seni destekliyorum. görelm yürüşünü. \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ba5122b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def vowel(letter):\n",
    "    \n",
    "    vowels = \"aeuioüöı\".split()\n",
    "    \n",
    "    if letter.lower() in vowels:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0cda1fc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "filtered_vowels = filter(vowel, cümle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e9aa28b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "print(*filtered_vowels)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c065f84b",
   "metadata": {},
   "source": [
    "### 15.03 Ders Çalışma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "331d7601",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your first name: Adam\n",
      "Your initial is: A\n"
     ]
    }
   ],
   "source": [
    "def get_initial(name):\n",
    "    initial = name[0:1].upper()\n",
    "    return initial\n",
    "first_name = input('Enter your first name: ')\n",
    "first_name_initial = get_initial(first_name)\n",
    "\n",
    "print('Your initial is: '+first_name_initial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "100cc5f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your first name: adam\n",
      "Your initial is: A\n"
     ]
    }
   ],
   "source": [
    "def get_initial(name, force_uppercase = False):\n",
    "    if force_uppercase:\n",
    "        initial = name[0:1].upper()\n",
    "    else:\n",
    "        initial = name[0:1]\n",
    "    return initial\n",
    "first_name = input('Enter your first name: ')\n",
    "first_name_initial = get_initial(first_name, True)\n",
    "\n",
    "print('Your initial is: '+first_name_initial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7c98a8c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The teams in Premier League are :\n",
      "- Liverpool\n",
      "- M.United\n",
      "- M.City\n",
      "- Arsenal\n"
     ]
    }
   ],
   "source": [
    "def team_names(*teams) :\n",
    "    print('The teams in Premier League are :')\n",
    "    for i in teams :\n",
    "        print('-', i)\n",
    "\n",
    "team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "68b446e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love Clarusway!\n"
     ]
    }
   ],
   "source": [
    "def make_sentence(**kwargs):\n",
    "    result = \"\"\n",
    "    # Iterating over the Python kwargs dictionary\n",
    "    for i in kwargs.values():\n",
    "        result += i\n",
    "    return result\n",
    "\n",
    "print(make_sentence(a=\"I \", b=\"love \", c=\"Clarusway!\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61eb457c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d5b0e54",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "721bfe08",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b636883f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "217bf52a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c5ef9db",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "620979fc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b20da005",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c71bc3b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8a7b056",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

