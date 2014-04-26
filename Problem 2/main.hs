sumfib x term1 term2 = if term2 < 4000000
							then if term2 `mod` 2 == 0
								then sumfib (x + term2) term2 (term1 + term2)
								else sumfib x term2 (term1 + term2)
							else x

main = print (sumfib 0 1 1)
