#include <iostream>

int main() {
	int a = 1;
	int b = 1;
	int sum = 0;
	
	do {
		if (b % 2 == 0) {
			sum += b;
		}

		int temp = b;
		b = a + b;
		a = temp;

	} while (b < 4000000);

	std::cout << sum << std::endl;
}
