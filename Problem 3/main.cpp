#include <iostream>
#include <cmath>

bool isPrime(uint64_t num) {
	uint64_t max = std::sqrt(num);
	if (num % 2 == 0) {
		return false;
	}

	for (uint64_t i = 3; i < max; i += 2) {
		if (num % i == 0) {
			return false;
		}
	}

	return true;
}

int main() {
	uint64_t num = 600851475143;
	uint64_t max = std::sqrt(num);
	uint64_t largest = 1;

	for (uint64_t i = 3; i < max; i++) {
		if (num % i == 0) {
			std::cout << "Found factor: " << i << std::endl;
			if (isPrime(i) && i > largest) {
				largest = i;
			}
			uint64_t otherFactor = num / i;
			if (isPrime(otherFactor) && otherFactor > largest) {
				largest = i;
			}
		}	
	}	
	std::cout << "Largest factor is: " << largest << std::endl;
}
