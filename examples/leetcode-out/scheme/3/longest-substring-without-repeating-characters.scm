(define (lengthOfLongestSubstring s)
	(call/cc (lambda (return)
		(define best '())
		(define i '())
		(define j '())
		(define length '())
		(define n '())
		(define start '())
		(set! n (length s))
		(set! start 0)
		(set! best 0)
		(set! i 0)
		(let loop ()
			(if (< i n)
				(begin
					(set! j start)
					(let loop ()
						(if (< j i)
							(begin
								(if (= (string-ref s j) (string-ref s i))
									(begin
										(set! start (+ j 1))
									)
									'()
								)
								(set! j (+ j 1))
								(loop)
							)
						'())
					)
					(set! length (+ (- i start) 1))
					(if (> length best)
						(begin
							(set! best length)
						)
						'()
					)
					(set! i (+ i 1))
					(loop)
				)
			'())
		)
		(return best)
	))
)

