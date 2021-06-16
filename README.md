# daydream

  + cc fib.c -lm -o fib
  
  + the constant time function uses the ODE solving method of the F(n) = F(n-1) + F(n-2) ==> x^2 = x + 1 i.e. the golden ratio.
  
  + F(n) = A * (1 + sqrt(5))/2 + B * (1 - sqrt(5))/2
  
  + solving with base conditions F(0)==0 and F(1)==1 renders F(n) = (1 / sqrt(5)) * ( (1 + sqrt(5))/2 - (1 - sqrt(5))/2 )

  + both the python and c code loose equality between the constant and optimized recurisve fib functions at n==72.
  
  + this signifies that they "may" be using the same api for calculation of the sqrt function.


## Sites

  + https://godbolt.org/

  + https://vitalik.ca/general/2019/05/12/fft.html

  + https://vitalik.ca/general/2019/04/01/cantor.html
