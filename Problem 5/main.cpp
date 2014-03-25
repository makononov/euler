#include <cstdio>
#include <cmath>
#include <map>
#include <vector>

void factors(std::vector<int>* factors, int num) {
	int i = 2;
	while (i <= num) {
		if (num % i == 0) {
			factors->push_back(i);
			num /= i;
			i = 2;
		}
		else {
			i++;
		}
	}
}

void factorCount(std::map<int, int>* counts, std::vector<int>* factors) {
	for (std::vector<int>::iterator fac = factors->begin(); fac != factors->end(); ++fac) {
		if (counts->find(*fac) != counts->end()) {
			(*counts)[*fac]++;
		}
		else {
			(*counts)[*fac] = 1;
		}
	}
}

int main(int argc, char* argv[]) {
	int primes[8] = {2, 3, 5, 7, 11, 13, 17, 19};
	std::map<int, int> primeCounts;

	for (int i = 0; i < 8; i++) {
		primeCounts[primes[i]] = 1;
	}

	std::vector<int>* f = new std::vector<int>;
	std::map<int, int>* counts = new std::map<int, int>;
	for (int i = 2; i <= 20; i++) {
		factors(f, i);
		factorCount(counts, f);
		for (std::map<int,int>::iterator fac = counts->begin(); fac != counts->end(); ++fac) {
			if (primeCounts[fac->first] < fac->second) {
				primeCounts[fac->first] = fac->second;		
			}
		}
		f->resize(0);
		counts->clear();
	}
	delete f;
	delete counts;

	unsigned int product = 1;
	for (std::map<int,int>::iterator c = primeCounts.begin(); c != primeCounts.end(); ++c) {
		product *= std::pow(c->first, c->second);
	}

	printf("The product is: %d\n", product);

	return 0;
}
