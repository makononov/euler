accum x list = if list == []
				then x
				else let num = head list 
					 in	if num `mod` 3 == 0 || num `mod` 5 == 0
						then accum (x+num) (tail list)
						else accum x (tail list)

answer = accum 0 [1..1000-1]

main = print answer
