#include <cstdio>
#include <cmath>

int numDigits(int num) {
	// Special cases for 0 and 1...
	if (num == 0) {
		return 0;
	}
	if (num == 1) {
		return 1;
	}

	return std::ceil(std::log10(std::abs(num)));
}	

int digitAt(int num, int index) {
	int digit;
	digit = num / (int)std::pow(10, index);
	digit %= 10; 
	return digit;
}

int isPalindrome(int num, int digits) {
	if (digits == 1 || digits == 0) {
		return true;
	}
	if (digitAt(num, digits - 1) != digitAt(num, 0)) {
		return false;
	}
	
	return isPalindrome((num % (int)std::pow(10, digits - 1)) / 10, digits - 2);
}

int main(int argc, char* argv[]) {
	int largest = 0;
	for (int i = 100; i < 1000; i++) {
		for (int j = 100; j < 1000; j++) {
			int product = i * j;
			if (isPalindrome(product, numDigits(product)) && product > largest) {
				largest = product;
			}
		}
	}

	printf("Largest palindrome found: %d\n", largest);
}
