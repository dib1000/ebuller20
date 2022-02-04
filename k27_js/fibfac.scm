;short (Emma Buller and Shyne Choi)
;SoftDev
;K27 -- Where Does JS live?
;2022-02-04
;time spent: 30
(define fact
  (lambda (n)
    (if (= n 1)
        1
        (* n (fact (- n 1))))))

(define fib
  (lambda (n)
    (if (< n 1)
        0
        (if (< n 2)
            1
            (+ (fib (- n 1)) (fib (- n 2)))))))
