# Week 7 Lab 7 Software Testing
# Main
import sieve_of_erastosthenes

input_number = int(input("number here: "))

first = sieve_of_erastosthenes.SieveOfErastosthenes()
res = first.compute_primes(input_number)

