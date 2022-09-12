{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb48cf13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type precision: 0.003\n",
      "Found solution after 3 iterations.\n",
      "0.18739309890220732\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "def newton(f,Df,x0,epsilon,max_iter):\n",
    "    xn = x0\n",
    "    for n in range(0,max_iter):\n",
    "        fxn = f(xn)\n",
    "        if abs(fxn) < epsilon:\n",
    "            print('Found solution after',n,'iterations.')\n",
    "            return xn\n",
    "        Dfxn = Df(xn)\n",
    "        if Dfxn == 0:\n",
    "            print('Zero derivative. No solution found.')\n",
    "            return None\n",
    "        xn = xn - fxn/Dfxn\n",
    "    print('Exceeded maximum iterations. No solution found.')\n",
    "    return None\n",
    "\n",
    "f=lambda x: math.log(x)+(x+1)**3\n",
    "Df=lambda x:1/x+3*x**2+6*x+3\n",
    "epsilon=float(input('Type precision: '))\n",
    "approx=newton(f,Df,1,epsilon,10)\n",
    "print(approx)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b33789b5",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
